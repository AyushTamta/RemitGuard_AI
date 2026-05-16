import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from ai.risk_engine import analyze_transaction_risk

from ai.document_engine import analyze_document

from reports.compliance_reporting_engine import (
    generate_report
)


st.set_page_config(
    page_title="RemitGuard Globe",
    layout="wide"
)


# ---------------- CSS ----------------
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0E1117;
    color: white;
}

.main-title {
    font-size:42px;
    font-weight:700;
    color:#00E0FF;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🌍 RemitGuard Globe</div>',
    unsafe_allow_html=True
)

st.caption(
    "Cross-Border Remittance Intelligence Platform"
)

st.markdown("---")


# ---------------- SIDEBAR ----------------
st.sidebar.title("Transaction Intelligence")

country = st.sidebar.selectbox(
    "Sender Country",
    ["USA", "UAE", "Singapore", "UK"]
)

amount = st.sidebar.number_input(
    "Transfer Amount ($)",
    min_value=100,
    max_value=100000,
    value=12000
)

frequency = st.sidebar.slider(
    "Transaction Frequency",
    1,
    15,
    4
)

new_beneficiary = st.sidebar.selectbox(
    "New Beneficiary",
    ["No", "Yes"]
)

new_beneficiary = (
    1 if new_beneficiary == "Yes"
    else 0
)


# ---------------- LAYOUT ----------------
left, right = st.columns([1, 1])


# ---------------- DOCUMENT ----------------
with left:

    st.subheader("📄 Document Intelligence")

    uploaded_file = st.file_uploader(
        "Upload Banking Document",
        type=["pdf", "png", "jpg"]
    )

    if uploaded_file:

        result = analyze_document(uploaded_file)

        st.success("Document Processed")

        st.markdown("### Extracted Entities")

        st.json(result["entities"])

        st.markdown("### AI Investigation Notes")

        st.info(result["investigation_summary"])

        st.markdown("### Compliance Flags")

        for flag in result["compliance_flags"]:
            st.warning(flag)


# ---------------- RISK DASHBOARD ----------------
with right:

    st.subheader("📊 Risk Intelligence Dashboard")

    if st.button("🚀 Analyze Transaction"):

        risk_result = analyze_transaction_risk(
            amount,
            frequency,
            country,
            new_beneficiary
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Risk Level",
                risk_result["risk_level"]
            )

        with col2:
            st.metric(
                "Risk Score",
                risk_result["risk_score"]
            )

        with col3:
            st.metric(
                "Confidence",
                f"{risk_result['confidence']}%"
            )


        # ---------------- GAUGE ----------------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_result["risk_score"],
            title={'text': "Risk Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 40], 'color': "green"},
                    {'range': [40, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "red"},
                ],
            }
        ))

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown(
            "### Behavioral Risk Indicators"
        )

        for flag in risk_result["behavioral_flags"]:
            st.warning(flag)

        st.markdown(
            "### AI Investigation Summary"
        )

        st.info(risk_result["summary"])

        st.markdown(
            "### Recommended Action"
        )

        if risk_result["risk_level"] == "High":

            st.error(
                "Enhanced Due Diligence Required"
            )

        else:

            st.success(
                "Transaction Approved"
            )

        report_path = generate_report(
            risk_result
        )

        with open(report_path, "rb") as file:

            st.download_button(
                label="📥 Download Compliance Report",
                data=file,
                file_name="remitguard_report.pdf"
            )