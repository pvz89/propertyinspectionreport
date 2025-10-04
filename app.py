import streamlit as st

# You can include CSS via this method
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def app():
    st.set_page_config(page_title="Property Inspection Report London", layout="wide")

    # If you have a CSS file in your repo, e.g. styles.css
    local_css("styles.css")
    # Or if you have online CSS (Bootstrap etc)
    # remote_css("https://path/to/your/stylesheet.css")

    # Header / Navigation
    st.markdown("""
    <div class="header">
      <h1>Property Inspection Report London</h1>
      <p>Fast, trusted service for UK visa applications. Get your Property Inspection Report within 24 hours.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Services section
    st.header("Our Property Inspection Report Services")
    st.subheader("Spouse Visa Inspection")
    st.write("Comprehensive property inspection reports specifically for spouse visa …")
    st.subheader("Family Visa Inspection")
    st.write("Property assessments for family visa applications …")
    st.subheader("24-Hour Emergency Service")
    st.write("Need an urgent inspection? We offer 24-hour notice ...")

    st.markdown("---")

    # Areas We Cover
    st.header("Areas We Cover")
    st.write("""
    - **London**: All London boroughs  
    - **South East**: Kent, Surrey, Essex, Sussex  
    - **Midlands**: Birmingham, Coventry, Leicester  
    - **North West**: Manchester, Liverpool  
    - **South West**: Bristol, Bournemouth  
    - **Wales, Scotland, Northern Ireland**  
    """)

    st.markdown("---")

    # Process
    st.header("Our Simple Process")
    st.write("""
    1. Contact Us  
    2. Property Visit  
    3. Receive Report  
    """)

    st.markdown("---")

    # FAQs
    st.header("Frequently Asked Questions")
    st.write("**What is a Property Inspection Report?** ...")
    st.write("**How quickly can I get my report?** ...")
    st.write("**Do you cover my area?** …")
    st.write("**What visas require P.I.R.?** …")

    st.markdown("---")

    # Testimonials / reviews
    st.header("What Our Clients Say")
    st.write('"Saju delivered excellent customer service …" — RG')
    st.write('"Saju is a true professional …" — IK')
    st.write('"Very professional, arrived on time …" — KA / Kay')

    st.markdown("---")

    # Contact form
    st.header("Contact Us")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        phone = st.text_input("Phone Number")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            # Here you would handle the form (e.g. send email, store to DB)
            st.success("Thank you — your message has been sent!")

    # Footer
    st.markdown("""
    <footer>
      <p>© 2025 Property Inspection Report – All Rights Reserved.</p>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
