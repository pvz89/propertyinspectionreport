import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Quality Home Services | Your Trusted Local Professionals",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .service-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        border-left: 5px solid #2E86AB;
        margin-bottom: 1rem;
    }
    .contact-form {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
    }
    .testimonial {
        font-style: italic;
        color: #555;
        border-left: 3px solid #2E86AB;
        padding-left: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<h1 class="main-header">Quality Home Services</h1>', unsafe_allow_html=True)
    st.markdown("### Your Trusted Local Professionals")
    st.markdown("---")

# Hero Section
st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h2 style='color: #2E86AB;'>Professional Home Services in Your Area</h2>
    <p style='font-size: 1.2rem;'>Reliable, affordable, and quality service you can trust. Serving the local community for over 10 years.</p>
</div>
""", unsafe_allow_html=True)

# Services Section
st.header("🏠 Our Services")
st.markdown("We offer a wide range of professional home services:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='service-card'>
        <h3>🔧 Plumbing</h3>
        <p>Leaky faucets, pipe repairs, installation, and more</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='service-card'>
        <h3>⚡ Electrical</h3>
        <p>Wiring, lighting, panel upgrades, and repairs</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='service-card'>
        <h3>🎨 Painting</h3>
        <p>Interior & exterior painting with quality materials</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='service-card'>
        <h3>🔨 Handyman</h3>
        <p>General repairs, assembly, and maintenance</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='service-card'>
        <h3>🧹 Cleaning</h3>
        <p>Deep cleaning, move-in/out, and regular maintenance</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='service-card'>
        <h3>🌿 Landscaping</h3>
        <p>Lawn care, gardening, and outdoor maintenance</p>
    </div>
    """, unsafe_allow_html=True)

# Why Choose Us Section
st.header("⭐ Why Choose Us?")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💰 Affordable")
    st.markdown("Competitive pricing with no hidden fees")

with col2:
    st.markdown("### ⏰ Reliable")
    st.markdown("On-time service with guaranteed quality")

with col3:
    st.markdown("### 🛠️ Experienced")
    st.markdown("10+ years serving the local community")

# Testimonials Section
st.header("📝 Customer Testimonials")
testimonials = [
    {"name": "Sarah M.", "text": "Outstanding service! They fixed my plumbing issue quickly and professionally."},
    {"name": "Mike R.", "text": "Fair pricing and excellent work. Will definitely use again!"},
    {"name": "Lisa T.", "text": "The team was punctual, clean, and did a fantastic job painting our house."}
]

cols = st.columns(3)
for idx, testimonial in enumerate(testimonials):
    with cols[idx]:
        st.markdown(f"""
        <div class='testimonial'>
            "{testimonial['text']}"
            <br><br>
            <strong>- {testimonial['name']}</strong>
        </div>
        """, unsafe_allow_html=True)

# Contact Form Section
st.header("📞 Get a Free Quote")
st.markdown("Fill out the form below and we'll get back to you within 24 hours:")

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name *")
        email = st.text_input("Email Address *")
        phone = st.text_input("Phone Number")
    
    with col2:
        service_type = st.selectbox(
            "Service Needed *",
            ["Select a service", "Plumbing", "Electrical", "Painting", "Handyman", "Cleaning", "Landscaping", "Other"]
        )
        address = st.text_input("Service Address")
    
    message = st.text_area("Describe your service needs *")
    
    submitted = st.form_submit_button("Submit Request")
    
    if submitted:
        if name and email and message and service_type != "Select a service":
            st.success("✅ Thank you! We've received your request and will contact you within 24 hours.")
        else:
            st.error("❌ Please fill in all required fields (*)")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📍 Location")
    st.markdown("""
    Serving Your Local Area
    """)

with col2:
    st.markdown("### 📞 Contact")
    st.markdown("""
    Phone: (555) 123-4567  
    Email: info@qualityhomeservices.com  
    Hours: Mon-Sun 7AM-7PM
    """)

with col3:
    st.markdown("### 💼 Business Info")
    st.markdown("""
    Licensed & Insured  
    Free Estimates  
    24/7 Emergency Service
    """)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'>© 2024 Quality Home Services. All rights reserved.</div>", unsafe_allow_html=True)
