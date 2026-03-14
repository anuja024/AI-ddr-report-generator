import streamlit as st
from pdf_parser import extract_text, extract_images
from ddr_generator import generate_ddr
from fpdf import FPDF

st.title("AI DDR Report Generator")

inspection_file = st.file_uploader("Upload Inspection Report", type="pdf")
thermal_file = st.file_uploader("Upload Thermal Report", type="pdf")


if inspection_file and thermal_file:

    if st.button("Generate DDR Report"):

        inspection_text = extract_text(inspection_file)
        thermal_file.seek(0)
        thermal_text = extract_text(thermal_file)

        thermal_file.seek(0)
        thermal_images = extract_images(thermal_file)


        report = generate_ddr(inspection_text, thermal_text)
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf_bytes = pdf.output(dest="S").encode("latin-1")
        st.download_button(
            "Download DDR Report",
            pdf_bytes,
            file_name="DDR_Report.pdf",
            mime="application/pdf"
        )

        st.subheader("Generated DDR Report")
        st.markdown(report)

        clean_report = report.replace("**","").replace("|","").replace("*","")
        clean_report = clean_report.replace("---","")

        for line in clean_report.split("\n"):
            pdf.multi_cell(0,10,line)
            pdf.ln(1)
        

        pdf.multi_cell(0,10,"Thermal Inspection Images:")
        pdf.ln(5)
        
        for img in thermal_images[::10]:
            pdf.add_page()
            pdf.image(img, x=10, y=20, w=180)
        
        

        st.subheader("Thermal Images Preview")

        for img in thermal_images[:5]:
            st.image(img, caption="Thermal Inspection Image", use_container_width=True)

        