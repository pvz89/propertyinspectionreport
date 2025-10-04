import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Green Vision - Property Inspection Reports",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern design
st.markdown("""
<style>
    /* Hide all Streamlit branding and code elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #ffffff; }
    
    /* Modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* Header styling */
    .main-header { 
        background: white; 
        padding: 1rem 0; 
        border-bottom: 1px solid #e5e7eb;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 6rem 2rem;
        border-radius: 0 0 30px 30px;
        color: white;
        text-align: center;
    }
    
    /* Modern cards */
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #f1f5f9;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    /* Stats styling */
    .stat-item {
        text-align: center;
        padding: 1.5rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1e40af;
        margin-bottom: 0.5rem;
    }
    
    /* Service cards */
    .service-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        border-left: 4px solid #3b82f6;
        height: 100%;
        transition: all 0.3s ease;
    }
    
    .service-card:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    /* Button styling */
    .primary-button {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        padding: 12px 32px;
        border-radius: 50px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .primary-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
        color: white;
    }
    
    .secondary-button {
        background: transparent;
        color: #3b82f6;
        padding: 12px 32px;
        border-radius: 50px;
        border: 2px solid #3b82f6;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .secondary-button:hover {
        background: #3b82f6;
        color: white;
    }
    
    /* Section headers */
    .section-title {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #64748b;
        margin-bottom: 3rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Testimonial cards */
    .testimonial-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        position: relative;
    }
    
    .testimonial-card::before {
        content: '"';
        font-size: 4rem;
        color: #3b82f6;
        opacity: 0.2;
        position: absolute;
        top: 10px;
        left: 20px;
    }
    
    /* Feature tags */
    .feature-tag {
        display: inline-flex;
        align-items: center;
        background: rgba(59, 130, 246, 0.1);
        color: #3b82f6;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 0.3rem;
        font-weight: 500;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 1, 1, 1, 1, 1, 1])

with col1:
    st.markdown("<h2 style='color: #1e40af; margin: 0;'>🏠 Green Vision</h2>", unsafe_allow_html=True)

with col2:
    if st.button("Home", use_container_width=True):
        pass

with col3:
    if st.button("Services", use_container_width=True):
        pass

with col4:
    if st.button("Areas", use_container_width=True):
        pass

with col5:
    if st.button("Process", use_container_width=True):
        pass

with col6:
    if st.button("Reviews", use_container_width=True):
        pass

with col7:
    if st.button("Contact", use_container_width=True):
        pass

st.markdown("---")

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1.5rem;">Professional Property Inspection Reports</h1>
    <p style="font-size: 1.3rem; margin-bottom: 2.5rem; opacity: 0.9;">Fast, reliable service for UK visa applications. Get your certified report within 24 hours.</p>
    
    <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 2.5rem;">
        <div class="feature-tag">
            <span style="margin-right: 8px;">✓</span> 24-Hour Service
        </div>
        <div class="feature-tag">
            <span style="margin-right: 8px;">✓</span> 100% Success Rate
        </div>
        <div class="feature-tag">
            <span style="margin-right: 8px;">✓</span> 12+ Years Experience
        </div>
    </div>
    
    <div style="display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
        <a href="https://www.propertyinspectionforimmigration.co.uk/contact" class="primary-button">Book Inspection Now</a>
        <a href="#services" class="secondary-button">Learn More</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats Section
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="background: white; padding: 3rem 2rem; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); margin: 2rem 0;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
        <div class="stat-item">
            <div class="stat-number">5000+</div>
            <div style="color: #64748b; font-weight: 600;">Properties Inspected</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">370+</div>
            <div style="color: #64748b; font-weight: 600;">5-Star Reviews</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">100%</div>
            <div style="color: #64748b; font-weight: 600;">Success Rate</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">24h</div>
            <div style="color: #64748b; font-weight: 600;">Fast Turnaround</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Services Section
st.markdown("<div class='section-title' id='services'>Our Inspection Services</div>", unsafe_allow_html=True)
st.markdown("<div class='section-subtitle'>Professional property inspection reports for all UK visa applications</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 3rem; color: #3b82f6; margin-bottom: 1rem;">📋</div>
        <h3 style="color: #1e293b; margin-bottom: 1rem;">Spouse Visa Inspection</h3>
        <p style="color: #64748b; margin-bottom: 1.5rem; line-height: 1.6;">Comprehensive property inspection reports specifically for spouse visa applications, meeting all UKVI requirements.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-spouse-visa/" class="primary-button" style="padding: 10px 20px; font-size: 0.9rem; text-decoration: none;">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 3rem; color: #3b82f6; margin-bottom: 1rem;">👨‍👩‍👧‍👦</div>
        <h3 style="color: #1e293b; margin-bottom: 1rem;">Family Visa Inspection</h3>
        <p style="color: #64748b; margin-bottom: 1.5rem; line-height: 1.6;">Property assessments for family visa applications ensuring your accommodation meets UK housing standards.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-family-visa-uk/" class="primary-button" style="padding: 10px 20px; font-size: 0.9rem; text-decoration: none;">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 3rem; color: #3b82f6; margin-bottom: 1rem;">⚡</div>
        <h3 style="color: #1e293b; margin-bottom: 1rem;">24-Hour Emergency Service</h3>
        <p style="color: #64748b; margin-bottom: 1.5rem; line-height: 1.6;">Need an urgent inspection? We offer 24-hour notice property inspections with fast report delivery.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/contact" class="primary-button" style="padding: 10px 20px; font-size: 0.9rem; text-decoration: none;">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

# Areas Covered Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Areas We Cover</div>", unsafe_allow_html=True)
st.markdown("<div class='section-subtitle'>We provide Property Inspection Reports throughout the UK</div>", unsafe_allow_html=True)

areas = [
    {"name": "London", "description": "All London boroughs"},
    {"name": "South East", "description": "Kent, Surrey, Essex, Sussex"},
    {"name": "Midlands", "description": "Birmingham, Coventry, Leicester"},
    {"name": "North West", "description": "Manchester, Liverpool"},
    {"name": "South West", "description": "Bristol, Bournemouth"},
    {"name": "Wales", "description": "Cardiff, Newport"},
    {"name": "Scotland", "description": "Glasgow, Edinburgh"},
    {"name": "Northern Ireland", "description": "Belfast, Derry"}
]

cols = st.columns(4)
for i, area in enumerate(areas):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 12px; text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.05); margin-bottom: 1rem; border: 1px solid #f1f5f9;">
            <div style="font-size: 2rem; color: #3b82f6; margin-bottom: 0.5rem;">📍</div>
            <h4 style="margin: 0 0 0.5rem 0; color: #1e293b;">{area['name']}</h4>
            <p style="margin: 0; color: #64748b; font-size: 0.9rem;">{area['description']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-top: 2rem;">
    <a href="https://www.propertyinspectionforimmigration.co.uk/areas-covered" class="primary-button" style="text-decoration: none;">View All Areas</a>
</div>
""", unsafe_allow_html=True)

# Process Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Our Simple Process</div>", unsafe_allow_html=True)
st.markdown("<div class='section-subtitle'>Get your Property Inspection Report in 3 easy steps</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 700; margin: 0 auto 1.5rem; box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);">1</div>
        <h3 style="color: #1e293b; margin-bottom: 1rem;">Contact Us</h3>
        <p style="color: #64748b; line-height: 1.6;">Call us or book online to schedule your property inspection at your convenience.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 700; margin: 0 auto 1.5rem; box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);">2</div>
        <h3 style="color: #1e293b; margin-bottom: 1rem;">Property Visit</h3>
        <p style="color: #64748b; line-height: 1.6;">Our certified surveyor visits your property within 24 hours to conduct a thorough inspection.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 700; margin: 0 auto 1.5rem; box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);">3</div>
        <h3 style="color: #1e293b; margin-bottom: 1rem;">Receive Report</h3>
        <p style="color: #64748b; line-height: 1.6;">Get your professional Property Inspection Report within 2 working days of the inspection.</p>
    </div>
    """, unsafe_allow_html=True)

# Testimonials Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Client Testimonials</div>", unsafe_allow_html=True)
st.markdown("<div class='section-subtitle'>Over 370 five-star reviews from satisfied customers</div>", unsafe_allow_html=True)

testimonials = [
    {
        "text": "Saju delivered excellent customer service, I required a property inspection on very short notice and he was able to attend the property within 1-2 hours of me calling him.",
        "author": "RippersGlory",
        "source": "Google Review"
    },
    {
        "text": "Saju is a true professional. From the initial phone call to the visit, everything was top-notch. He completed the full inspection and provided the certificate in less than 24 hours.",
        "author": "Imdad Khan",
        "source": "Google Review"
    },
    {
        "text": "Very professional, arrived on time and completed the report very quick. Highly recommend this company!",
        "author": "Kay",
        "source": "Google Review"
    }
]

cols = st.columns(3)
for i, testimonial in enumerate(testimonials):
    with cols[i]:
        st.markdown(f"""
        <div class="testimonial-card">
            <div style="color: #f59e0b; margin-bottom: 1rem; font-size: 1.2rem;">★★★★★</div>
            <p style="font-style: italic; color: #475569; margin-bottom: 1.5rem; line-height: 1.6;">"{testimonial['text']}"</p>
            <div style="display: flex; align-items: center;">
                <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-right: 1rem;">
                    {testimonial['author'][0]}
                </div>
                <div>
                    <h4 style="margin: 0; color: #1e293b;">{testimonial['author']}</h4>
                    <p style="margin: 0; color: #64748b; font-size: 0.9rem;">{testimonial['source']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# FAQ Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Frequently Asked Questions</div>", unsafe_allow_html=True)
st.markdown("<div class='section-subtitle'>Find answers to common questions about our Property Inspection Reports</div>", unsafe_allow_html=True)

faq_data = [
    {
        "question": "What is a Property Inspection Report?",
        "answer": "A Property Inspection Report is an official document confirming that a property is safe, habitable, and not overcrowded according to the Housing Act 1985. It's required for UK visa applications to prove suitable accommodation."
    },
    {
        "question": "How quickly can I get my report?",
        "answer": "We offer 24-hour short notice inspection visits and typically deliver your Property Inspection Report within 2 working days of the inspection being carried out."
    },
    {
        "question": "Do you cover my area?",
        "answer": "We cover every corner of the UK, including England, Wales, Scotland, and Northern Ireland. Our service is available in all major cities and towns across the country."
    },
    {
        "question": "What visas require a Property Inspection Report?",
        "answer": "Property Inspection Reports are typically required for spouse visas, partner visas, family visas, and other settlement applications where you need to prove suitable accommodation in the UK."
    }
]

for faq in faq_data:
    with st.expander(f"**{faq['question']}**", expanded=False):
        st.write(faq["answer"])

st.markdown("""
<div style="text-align: center; margin-top: 2rem;">
    <a href="https://www.propertyinspectionforimmigration.co.uk/frequently-asked-questions/" class="primary-button" style="text-decoration: none;">View All FAQs</a>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Contact Us</div>", unsafe_allow_html=True)
st.markdown("<div class='section-subtitle'>Get in touch for a fast Property Inspection Report</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div style="background: white; padding: 2.5rem; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.06);">
        <h3 style="color: #1e293b; margin-bottom: 1.5rem;">Get in Touch</h3>
        <p style="color: #64748b; margin-bottom: 2rem; line-height: 1.6;">For reliable Property Inspection Reports in London and across the UK, contact Green Vision Engineers today.</p>
        
        <div style="margin-bottom: 2rem;">
            <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                <div style="font-size: 1.5rem; color: #3b82f6; margin-right: 1rem;">📞</div>
                <div>
                    <h4 style="margin: 0; color: #1e293b;">Phone</h4>
                    <p style="margin: 0; color: #64748b;">Mobile: 07912 351 329</p>
                    <p style="margin: 0; color: #64748b;">Office: 020 3488 4930</p>
                </div>
            </div>
            
            <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                <div style="font-size: 1.5rem; color: #3b82f6; margin-right: 1rem;">✉️</div>
                <div>
                    <h4 style="margin: 0; color: #1e293b;">Email</h4>
                    <p style="margin: 0; color: #64748b;">info@propertyinspectionforimmigration.co.uk</p>
                </div>
            </div>
            
            <div style="display: flex; align-items: center; margin-bottom: 2rem;">
                <div style="font-size: 1.5rem; color: #3b82f6; margin-right: 1rem;">📍</div>
                <div>
                    <h4 style="margin: 0; color: #1e293b;">Office Address</h4>
                    <p style="margin: 0; color: #64748b;">241A Whitechapel Rd, London E1 1DB, United Kingdom</p>
                </div>
            </div>
        </div>
        
        <div style="border-radius: 12px; overflow: hidden; margin-bottom: 1rem;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3219.72147039414!2d-0.06103699999999998!3d51.51914529999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761ccdc867bd5f%3A0x433ee054e9fa1361!2sProperty%20Inspection%20Report%20for%20UK%20Visa%20and%20Immigration!5e1!3m2!1sen!2suk!4v1759083676101!5m2!1sen!2suk" width="100%" height="200" style="border:0; border-radius: 10px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <a href="https://www.google.com/maps?cid=4845556904404587361" target="_blank" style="color: #3b82f6; font-weight: 600; text-decoration: none; display: inline-block; margin-top: 0.5rem;">View on Google Maps ↗</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    with st.form("contact_form", clear_on_submit=True):
        st.markdown("### Book an Inspection")
        name = st.text_input("Your Name", placeholder="Enter your full name")
        email = st.text_input("Your Email", placeholder="Enter your email address")
        phone = st.text_input("Phone Number", placeholder="Enter your phone number")
        message = st.text_area("Your Message", placeholder="Tell us about your property inspection needs...", height=120)
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            st.success("✅ Thank you for your message! We will contact you shortly.")

# Footer
st.markdown("""
<div style="background: linear-gradient(135deg, #1e293b 0%, #334155 100%); color: white; padding: 3rem 2rem; border-radius: 20px 20px 0 0; margin-top: 4rem;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 3rem; margin-bottom: 3rem;">
        <div>
            <h3 style="color: white; margin-bottom: 1.5rem;">Green Vision Engineers</h3>
            <p style="color: #cbd5e1; line-height: 1.6;">Leading provider of Property Inspection Reports for UK visa applications with over 12 years of experience.</p>
            <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
                <a href="https://en-gb.facebook.com/gvecuk/" style="color: white; text-decoration: none; background: rgba(255,255,255,0.1); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">f</a>
                <a href="#" style="color: white; text-decoration: none; background: rgba(255,255,255,0.1); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">t</a>
            </div>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1.5rem;">Quick Links</h4>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">Home</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/our-surveyors/" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">Services</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/areas-covered" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">Areas Covered</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/about-us" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">About Us</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/contact" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">Contact Us</a></p>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1.5rem;">Our Services</h4>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/services" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">Spouse Visa Inspection</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-family-visa-uk/" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">Family Visa Inspection</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/contact" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">24-Hour Emergency Service</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/" style="color: #cbd5e1; text-decoration: none; display: block; margin-bottom: 0.5rem;">Property Inspection Report London</a></p>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1.5rem;">Contact Info</h4>
            <p style="color: #cbd5e1; margin-bottom: 0.5rem;">📞 07912 351 329</p>
            <p style="color: #cbd5e1; margin-bottom: 0.5rem;">📞 020 3488 4930</p>
            <p style="color: #cbd5e1; margin-bottom: 0.5rem;">✉️ info@propertyinspectionforimmigration.co.uk</p>
            <p style="color: #cbd5e1;">📍 241A Whitechapel Rd, London E1 1DB</p>
        </div>
    </div>
    
    <div style="text-align: center; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1);">
        <p style="color: #94a3b8; margin: 0;">© 2025 Green Vision Engineers - All Rights Reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)
