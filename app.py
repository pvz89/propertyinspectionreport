import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import requests

# Page configuration
st.set_page_config(
    page_title="Professional Property Inspection Services | London",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #A23B72;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    .section-header {
        font-size: 2.2rem;
        color: #2E86AB;
        margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #F18F01;
        padding-bottom: 0.5rem;
    }
    .service-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #F18F01;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .testimonial-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #2E86AB;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .contact-form {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stButton>button {
        background-color: #F18F01;
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #e68200;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="main-header">🏠 Professional Property Inspection Services</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Trusted Property Inspections Across London</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; font-size: 1.2rem; color: #555; margin-bottom: 2rem;'>
        Comprehensive property inspections by certified professionals. 
        Serving London and surrounding areas since 2010.
    </div>
    """, unsafe_allow_html=True)

# Hero Section
st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", 
         use_column_width=True, caption="Professional Property Inspections in London")

# Services Section
st.markdown('<div class="section-header">Our Inspection Services</div>', unsafe_allow_html=True)

services_col1, services_col2 = st.columns(2)

with services_col1:
    st.markdown("""
    <div class="service-card">
        <h3>🏘️ Residential Property Surveys</h3>
        <ul>
            <li>Home Buyer Reports</li>
            <li>Building Surveys</li>
            <li>Snagging Lists for New Builds</li>
            <li>Specific Defect Surveys</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <h3>🏢 Commercial Property Inspections</h3>
        <ul>
            <li>Commercial Building Surveys</li>
            <li>Dilapidation Surveys</li>
            <li>Condition Surveys</li>
            <li>Technical Due Diligence</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with services_col2:
    st.markdown("""
    <div class="service-card">
        <h3>🔍 Specialized Inspections</h3>
        <ul>
            <li>Damp and Timber Surveys</li>
            <li>Roof and Loft Inspections</li>
            <li>Electrical System Checks</li>
            <li>Plumbing and Heating Assessments</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="service-card">
        <h3>📊 Professional Reports</h3>
        <ul>
            <li>Detailed Digital Reports</li>
            <li>Photographic Evidence</li>
            <li>Repair Cost Estimates</li>
            <li>Priority Action Plans</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Why Choose Us Section
st.markdown('<div class="section-header">Why Choose Our Services?</div>', unsafe_allow_html=True)

benefits_col1, benefits_col2, benefits_col3 = st.columns(3)

with benefits_col1:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h3>🎓 Certified Experts</h3>
        <p>RICS & CIOB certified surveyors with 10+ years experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h3>⚡ Quick Turnaround</h3>
        <p>Reports delivered within 48 hours of inspection</p>
    </div>
    """, unsafe_allow_html=True)

with benefits_col2:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h3>💷 Competitive Pricing</h3>
        <p>Transparent pricing with no hidden costs</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h3>📱 Digital Reports</h3>
        <p>Interactive digital reports with photos and videos</p>
    </div>
    """, unsafe_allow_html=True)

with benefits_col3:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h3>🏆 5-Star Rated</h3>
        <p>Consistently rated 5 stars by our clients</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h3>🔧 Post-Inspection Support</h3>
        <p>Free consultation after your inspection</p>
    </div>
    """, unsafe_allow_html=True)

# Testimonials Section
st.markdown('<div class="section-header">What Our Clients Say</div>', unsafe_allow_html=True)

testimonial_col1, testimonial_col2 = st.columns(2)

with testimonial_col1:
    st.markdown("""
    <div class="testimonial-card">
        <p>"The survey was incredibly thorough and saved us from purchasing a property with serious structural issues. The report was clear and detailed."</p>
        <p><strong>Sarah M.</strong> - Kensington</p>
        <p>⭐️⭐️⭐️⭐️⭐️</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="testimonial-card">
        <p>"Professional service from start to finish. The surveyor spent over 3 hours inspecting the property and provided invaluable advice."</p>
        <p><strong>James T.</strong> - Islington</p>
        <p>⭐️⭐️⭐️⭐️⭐️</p>
    </div>
    """, unsafe_allow_html=True)

with testimonial_col2:
    st.markdown("""
    <div class="testimonial-card">
        <p>"As a first-time buyer, I found the process confusing until I used their services. They explained everything clearly and gave me peace of mind."</p>
        <p><strong>Emma L.</strong> - Camden</p>
        <p>⭐️⭐️⭐️⭐️⭐️</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="testimonial-card">
        <p>"The commercial property inspection was comprehensive and helped us negotiate a better price. Excellent value for money."</p>
        <p><strong>David R.</strong> - City of London</p>
        <p>⭐️⭐️⭐️⭐️⭐️</p>
    </div>
    """, unsafe_allow_html=True)

# Pricing Section
st.markdown('<div class="section-header">Our Pricing</div>', unsafe_allow_html=True)

pricing_data = {
    'Service Type': [
        'Home Buyer Report', 
        'Building Survey', 
        'Snagging List', 
        'Commercial Survey',
        'Specific Defect Survey'
    ],
    'Starting From': [
        '£450', 
        '£650', 
        '£350', 
        '£850',
        '£250'
    ],
    'Turnaround': [
        '48 hours', 
        '72 hours', 
        '24 hours', 
        '5 days',
        '24 hours'
    ],
    'Best For': [
        'Standard residential properties',
        'Older or unique properties',
        'New build properties',
        'Commercial buildings',
        'Specific concerns'
    ]
}

df = pd.DataFrame(pricing_data)
st.dataframe(df, use_container_width=True, hide_index=True)

# Contact Form Section
st.markdown('<div class="section-header">Book Your Inspection</div>', unsafe_allow_html=True)

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name *")
        email = st.text_input("Email Address *")
        phone = st.text_input("Phone Number *")
        
    with col2:
        property_type = st.selectbox(
            "Property Type *",
            ["Residential House", "Residential Flat", "Commercial", "Mixed Use", "Other"]
        )
        inspection_type = st.selectbox(
            "Inspection Type *",
            ["Home Buyer Report", "Building Survey", "Snagging List", "Commercial Survey", "Specific Defect", "Not Sure"]
        )
        postcode = st.text_input("Property Postcode *")
    
    message = st.text_area("Additional Information", placeholder="Tell us about your property and specific concerns...")
    
    preferred_date = st.date_input("Preferred Inspection Date", min_value=datetime.now().date())
    
    submitted = st.form_submit_button("Request Free Quote")
    
    if submitted:
        if name and email and phone and postcode:
            st.success("🎉 Thank you for your inquiry! We'll contact you within 24 hours to discuss your inspection needs.")
            
            # In a real app, you would send this data to your backend
            st.info(f"""
            **Submission Summary:**
            - Name: {name}
            - Email: {email}
            - Phone: {phone}
            - Property Type: {property_type}
            - Inspection Type: {inspection_type}
            - Postcode: {postcode}
            - Preferred Date: {preferred_date}
            """)
        else:
            st.error("Please fill in all required fields (*)")

# Contact Information
st.markdown('<div class="section-header">Contact Us</div>', unsafe_allow_html=True)

contact_col1, contact_col2, contact_col3 = st.columns(3)

with contact_col1:
    st.markdown("""
    <div style='text-align: center;'>
        <h3>📞 Phone</h3>
        <p>020 7123 4567</p>
        <p>Mon-Fri: 8am-6pm</p>
        <p>Sat: 9am-4pm</p>
    </div>
    """, unsafe_allow_html=True)

with contact_col2:
    st.markdown("""
    <div style='text-align: center;'>
        <h3>✉️ Email</h3>
        <p>info@propertyinspectionslondon.co.uk</p>
        <p>quotes@propertyinspectionslondon.co.uk</p>
    </div>
    """, unsafe_allow_html=True)

with contact_col3:
    st.markdown("""
    <div style='text-align: center;'>
        <h3>🏢 Office</h3>
        <p>123 Inspection House</p>
        <p>London, EC1A 1BB</p>
        <p>United Kingdom</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("""
    **Professional Property Inspection Services London**  
    RICS & CIOB Certified  
    Fully Insured & Accredited
    """)

with footer_col2:
    st.markdown("""
    **Quick Links**  
    [Services](#our-inspection-services) • 
    [Pricing](#our-pricing) • 
    [Contact](#contact-us)
    """)

with footer_col3:
    st.markdown("""
    **Connect With Us**  
    📱 LinkedIn • Twitter • Facebook
    """)

st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem;'>
    © 2024 Professional Property Inspection Services London. All rights reserved.
</div>
""", unsafe_allow_html=True)
