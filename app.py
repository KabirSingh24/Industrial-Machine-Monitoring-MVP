import streamlit as st
import pandas as pd
from sensors.temperature import read_temperature
from brain.analyzer import analyze_temperature
from utils.logger import log_data

st.title("Factory Machine Monitor")

page = st.sidebar.selectbox(
    "Select View",
    ["Live Monitor", "Analytics"]
)

# Base machine template
machines = {
    "M1": {"area": "Assembly", "history": []},
    "M2": {"area": "Assembly", "history": []},
    "M3": {"area": "Packaging", "history": []},
}

# Initialize session state ONCE
if "machine_data" not in st.session_state:
    st.session_state.machine_data = machines


if page == "Live Monitor":

    # Refresh button (OUTSIDE initialization block)
    if st.button("Refresh Data"):
        for machine_id, data in st.session_state.machine_data.items():
            temp = read_temperature()
            data["history"].append(temp)

    # Group machines by area
    areas = {}
    for machine_id, data in st.session_state.machine_data.items():
        area = data["area"]
        areas.setdefault(area, []).append((machine_id, data))

    # Display by area
    for area, machines_in_area in areas.items():
        st.header(f"Area: {area}")

        for machine_id, data in machines_in_area:

            if data["history"]:
                current = data["history"][-1]

                status, message = analyze_temperature(
                    data["history"][:-1],
                    current
                )

                # Log after computing status
                log_data(machine_id, data["area"], current, status)

                st.subheader(f"Machine {machine_id}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Temperature", f"{current} °C")

                with col2:
                    st.metric("Status", status)

                if status == "NORMAL":
                    st.success(message)
                elif status == "WARNING":
                    st.warning(message)
                else:
                    st.error(message)

                st.line_chart(data["history"])
                st.write("---")

            else:
                st.info("No data yet. Click Refresh Data.")
elif page == "Analytics":

    st.title("Machine Analytics")

    try:
        df = pd.read_csv(
            "data/logs.csv",
            names=["timestamp", "machine_id", "area", "temperature", "status"]
        )


        if not df.empty:
            st.dataframe(df.tail(20))

            machine_selected = st.selectbox(
                "Select Machine",
                df["machine_id"].unique()
            )

            machine_df = df[df["machine_id"] == machine_selected]

            st.line_chart(machine_df["temperature"])
        else:
            st.warning("Log file exists but contains no data.")

    except FileNotFoundError:
        st.warning("No historical data available yet.")
