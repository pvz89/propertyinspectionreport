import streamlit as st
import pandas as pd

# Configure the page
st.set_page_config(
    page_title="Property Inspection Report London | Fast UK Visa Inspection Service",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #f8fafc;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .card {
        background-color: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    
    .feature-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .service-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border-top: 3px solid #667eea;
    }
    
    .testimonial-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        border-left: 3px solid #10b981;
    }
    
    .area-card {
        background: white;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin: 0.5rem;
    }
    
    .btn-primary {
        background-color: #667eea;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        border: none;
        cursor: pointer;
    }
    
    .btn-secondary {
        background-color: transparent;
        color: #667eea;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        border: 2px solid #667eea;
        cursor: pointer;
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .contact-form {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# Navigation
col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 1, 1, 1, 1, 1, 1])
with col1:
    st.markdown("### 🏠 Green Vision Engineers")

with col2:
    if st.button("Home"):
        st.session_state.page = "home"

with col3:
    if st.button("Services"):
        st.session_state.page = "services"

with col4:
    if st.button("Areas"):
        st.session_state.page = "areas"

with col5:
    if st.button("About"):
        st.session_state.page = "about"

with col6:
    if st.button("Blog"):
        st.session_state.page = "blog"

with col7:
    if st.button("Contact"):
        st.session_state.page = "contact"

st.markdown("---")

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1 style="font-size: 3rem; margin-bottom: 1rem;">Property Inspection Report London</h1>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">Fast, trusted service for UK visa applications. Get your Property Inspection Report within 24 hours.</p>
    
    <div style="display: flex; gap: 1rem; margin-bottom: 2rem;">
        <div style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; display: inline-flex; align-items: center;">
            <span style="margin-right: 8px;">✓</span> 24-Hour Service
        </div>
        <div style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; display: inline-flex; align-items: center;">
            <span style="margin-right: 8px;">✓</span> 100% Success Rate
        </div>
        <div style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; display: inline-flex; align-items: center;">
            <span style="margin-right: 8px;">✓</span> 12+ Years Experience
        </div>
    </div>
    
    <div style="display: flex; gap: 1rem;">
        <a href="https://www.propertyinspectionforimmigration.co.uk/contact" style="background-color: white; color: #667eea; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600; display: inline-block;">Book Inspection Now</a>
        <a href="#services" style="background-color: transparent; color: white; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600; border: 2px solid white; display: inline-block;">Learn More</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Trust Section
st.markdown("""
<div class="stats-container">
    <div class="stat-item">
        <h2 style="color: #667eea; margin: 0;">5000+</h2>
        <p>Properties Inspected</p>
    </div>
    <div class="stat-item">
        <h2 style="color: #667eea; margin: 0;">370+</h2>
        <p>5-Star Reviews</p>
    </div>
    <div class="stat-item">
        <h2 style="color: #667eea; margin: 0;">100%</h2>
        <p>Success Rate</p>
    </div>
    <div class="stat-item">
        <h2 style="color: #667eea; margin: 0;">24h</h2>
        <p>Fast Turnaround</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Services Section
st.markdown('<div class="section-header" id="services"><h2>Our Property Inspection Report Services</h2><p>Professional property inspection reports for all UK visa applications</p></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <h3>📋 Spouse Visa Inspection</h3>
        <p>Comprehensive property inspection reports specifically for spouse visa applications, meeting all UKVI requirements.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-spouse-visa/" class="btn-primary">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <h3>👨‍👩‍👧‍👦 Family Visa Inspection</h3>
        <p>Property assessments for family visa applications ensuring your accommodation meets UK housing standards.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-family-visa-uk/" class="btn-primary">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <h3>⏰ 24-Hour Emergency Service</h3>
        <p>Need an urgent inspection? We offer 24-hour notice property inspections with fast report delivery.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/contact" class="btn-primary">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

# Areas Covered Section
st.markdown('<div class="section-header" id="areas"><h2>Areas We Cover</h2><p>We provide Property Inspection Reports throughout the UK</p></div>', unsafe_allow_html=True)

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
        <div class="area-card">
            <h4>📍 {area['name']}</h4>
            <p>{area['description']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div style="text-align: center; margin-top: 2rem;"><a href="https://www.propertyinspectionforimmigration.co.uk/areas-covered" class="btn-primary">View All Areas</a></div>', unsafe_allow_html=True)

# Process Section
st.markdown('<div class="section-header" id="process"><h2>Our Simple Process</h2><p>Get your Property Inspection Report in 3 easy steps</p></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem;">
        <div style="width: 60px; height: 60px; background-color: #667eea; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin: 0 auto 1rem;">1</div>
        <h3>Contact Us</h3>
        <p>Call us or book online to schedule your property inspection at your convenience.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem;">
        <div style="width: 60px; height: 60px; background-color: #667eea; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin: 0 auto 1rem;">2</div>
        <h3>Property Visit</h3>
        <p>Our certified surveyor visits your property within 24 hours to conduct a thorough inspection.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem;">
        <div style="width: 60px; height: 60px; background-color: #667eea; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; margin: 0 auto 1rem;">3</div>
        <h3>Receive Report</h3>
        <p>Get your professional Property Inspection Report within 2 working days of the inspection.</p>
    </div>
    """, unsafe_allow_html=True)

# FAQ Section
st.markdown('<div class="section-header" id="faq"><h2>Frequently Asked Questions</h2><p>Find answers to common questions about our Property Inspection Reports</p></div>', unsafe_allow_html=True)

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
    with st.expander(faq["question"]):
        st.write(faq["answer"])

st.markdown('<div style="text-align: center; margin-top: 2rem;"><a href="https://www.propertyinspectionforimmigration.co.uk/frequently-asked-questions/" class="btn-primary">View All FAQs</a></div>', unsafe_allow_html=True)

# Testimonials Section
st.markdown('<div class="section-header" id="testimonials"><h2>What Our Clients Say</h2><p>Over 370 five-star reviews from satisfied customers</p></div>', unsafe_allow_html=True)

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
            <div style="color: #f59e0b; margin-bottom: 1rem;">★★★★★</div>
            <p style="font-style: italic;">"{testimonial['text']}"</p>
            <div style="display: flex; align-items: center; margin-top: 1rem;">
                <div style="width: 40px; height: 40px; background-color: #10b981; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-right: 1rem;">
                    {testimonial['author'][0]}
                </div>
                <div>
                    <h4 style="margin: 0;">{testimonial['author']}</h4>
                    <p style="margin: 0; color: #64748b;">{testimonial['source']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Blog Section
st.markdown('<div class="section-header" id="blog"><h2>Latest Blog Posts</h2><p>Helpful information about UK visas and property inspections</p></div>', unsafe_allow_html=True)

blog_posts = [
    {
        "title": "Understanding UK Visa Property Requirements",
        "date": "May 15, 2023",
        "excerpt": "Learn about the property requirements for UK visa applications and how to ensure your accommodation meets all the necessary standards.",
        "link": "https://www.propertyinspectionforimmigration.co.uk/blog/understanding-uk-visa-property-requirements"
    },
    {
        "title": "What to Expect During a Property Inspection",
        "date": "April 28, 2023",
        "excerpt": "A step-by-step guide to the property inspection process, helping you prepare for your upcoming assessment.",
        "link": "https://www.propertyinspectionforimmigration.co.uk/blog/what-to-expect-during-property-inspection"
    },
    {
        "title": "Common Spouse Visa Application Mistakes",
        "date": "April 10, 2023",
        "excerpt": "Avoid these common mistakes when applying for a spouse visa to ensure a smooth application process.",
        "link": "https://www.propertyinspectionforimmigration.co.uk/blog/common-spouse-visa-mistakes"
    }
]

cols = st.columns(3)
for i, post in enumerate(blog_posts):
    with cols[i]:
        st.markdown(f"""
        <div style="background: white; border-radius: 10px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05); height: 100%;">
            <p style="color: #64748b; margin-bottom: 0.5rem;">{post['date']}</p>
            <h3 style="margin-bottom: 1rem;">{post['title']}</h3>
            <p style="color: #64748b; margin-bottom: 1.5rem;">{post['excerpt']}</p>
            <a href="{post['link']}" style="color: #667eea; font-weight: 600; text-decoration: none;">Read More →</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div style="text-align: center; margin-top: 2rem;"><a href="https://www.propertyinspectionforimmigration.co.uk/blog" class="btn-primary">View All Blog Posts</a></div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="section-header" id="contact"><h2>Contact Us</h2><p>Get in touch for a fast Property Inspection Report</p></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
        <h3>Get in Touch</h3>
        <p>For reliable Property Inspection Reports in London and across the UK, contact Green Vision Engineers today.</p>
        
        <div style="margin-top: 2rem;">
            <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
                <div style="font-size: 1.3rem; color: #667eea; margin-right: 1rem;">📞</div>
                <div>
                    <h4 style="margin: 0;">Phone</h4>
                    <p style="margin: 0;">Mobile: 07912 351 329</p>
                    <p style="margin: 0;">Office: 020 3488 4930</p>
                </div>
            </div>
            
            <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
                <div style="font-size: 1.3rem; color: #667eea; margin-right: 1rem;">✉️</div>
                <div>
                    <h4 style="margin: 0;">Email</h4>
                    <p style="margin: 0;">info@propertyinspectionforimmigration.co.uk</p>
                </div>
            </div>
            
            <div style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
                <div style="font-size: 1.3rem; color: #667eea; margin-right: 1rem;">📍</div>
                <div>
                    <h4 style="margin: 0;">Office Address</h4>
                    <p style="margin: 0;">241A Whitechapel Rd, London E1 1DB, United Kingdom</p>
                </div>
            </div>
        </div>
        
        <div style="margin-top: 2rem;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3219.72147039414!2d-0.06103699999999998!3d51.51914529999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761ccdc867bd5f%3A0x433ee054e9fa1361!2sProperty%20Inspection%20Report%20for%20UK%20Visa%20and%20Immigration!5e1!3m2!1sen!2suk!4v1759083676101!5m2!1sen!2suk" width="100%" height="200" style="border:0; border-radius: 8px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            <a href="https://www.google.com/maps?cid=4845556904404587361" target="_blank" style="color: #667eea; font-weight: 600; text-decoration: none; margin-top: 0.5rem; display: inline-block;">View on Google Maps ↗</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    with st.form("contact_form"):
        st.markdown("### Book an Inspection")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        phone = st.text_input("Phone Number")
        message = st.text_area("Your Message", placeholder="Tell us about your property inspection needs...")
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            st.success("Thank you for your message! We will contact you shortly.")

# Footer
st.markdown("---")
st.markdown("""
<div style="background-color: #1e293b; color: white; padding: 3rem 2rem; border-radius: 10px; margin-top: 3rem;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
        <div>
            <h3 style="color: white; margin-bottom: 1rem;">Green Vision Engineers</h3>
            <p>Leading provider of Property Inspection Reports for UK visa applications with over 12 years of experience.</p>
            <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                <a href="https://en-gb.facebook.com/gvecuk/" style="color: white; text-decoration: none;">Facebook</a>
                <a href="#" style="color: white; text-decoration: none;">Twitter</a>
            </div>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1rem;">Quick Links</h4>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/" style="color: #cbd5e1; text-decoration: none;">Home</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/our-surveyors/" style="color: #cbd5e1; text-decoration: none;">Services</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/areas-covered" style="color: #cbd5e1; text-decoration: none;">Areas Covered</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/about-us" style="color: #cbd5e1; text-decoration: none;">About Us</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/contact" style="color: #cbd5e1; text-decoration: none;">Contact Us</a></p>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1rem;">Our Services</h4>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/services" style="color: #cbd5e1; text-decoration: none;">Spouse Visa Inspection</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-family-visa-uk/" style="color: #cbd5e1; text-decoration: none;">Family Visa Inspection</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/contact" style="color: #cbd5e1; text-decoration: none;">24-Hour Emergency Service</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/" style="color: #cbd5e1; text-decoration: none;">Property Inspection Report London</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/areas-covered" style="color: #cbd5e1; text-decoration: none;">Nationwide Coverage</a></p>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1rem;">Contact Info</h4>
            <p style="color: #cbd5e1;">📞 07912 351 329</p>
            <p style="color: #cbd5e1;">📞 020 3488 4930</p>
            <p style="color: #cbd5e1;">✉️ info@propertyinspectionforimmigration.co.uk</p>
            <p style="color: #cbd5e1;">📍 241A Whitechapel Rd, London E1 1DB</p>
        </div>
    </div>
    
    <div style="text-align: center; padding-top: 2rem; border-top: 1px solid #334155;">
        <p style="color: #94a3b8;">© 2025 Property Inspection Report - All Rights Reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)
