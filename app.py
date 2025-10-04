import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Property Inspection Report London | Fast UK Visa Inspection Service",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for new design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Modern header */
    .modern-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 0 0 20px 20px;
        padding: 1rem 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    
    /* Glass morphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }
    
    /* Gradient buttons */
    .gradient-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        text-align: center;
    }
    
    .gradient-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        color: white;
    }
    
    .outline-btn {
        background: transparent;
        color: #667eea;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        border: 2px solid #667eea;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        text-align: center;
    }
    
    .outline-btn:hover {
        background: #667eea;
        color: white;
        transform: translateY(-2px);
    }
    
    /* Stats with icons */
    .stat-card {
        text-align: center;
        padding: 2rem 1rem;
    }
    
    .stat-icon {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem;
        font-size: 2rem;
        color: white;
    }
    
    /* Service cards with hover effects */
    .service-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        height: 100%;
        border-top: 4px solid #667eea;
    }
    
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
    }
    
    /* Testimonial cards */
    .testimonial-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        position: relative;
        margin-bottom: 2rem;
    }
    
    .testimonial-card::before {
        content: '"';
        font-size: 4rem;
        color: #667eea;
        opacity: 0.2;
        position: absolute;
        top: 10px;
        left: 20px;
    }
    
    /* Feature tags */
    .feature-tag {
        display: inline-flex;
        align-items: center;
        background: rgba(102, 126, 234, 0.1);
        color: #667eea;
        padding: 8px 16px;
        border-radius: 25px;
        margin: 0.5rem;
        font-weight: 500;
    }
    
    /* Section headers */
    .section-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    /* Navigation */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    
    .nav-link {
        color: #333;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
        padding: 0.5rem 1rem;
        border-radius: 25px;
    }
    
    .nav-link:hover {
        color: #667eea;
        background: rgba(102, 126, 234, 0.1);
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 5rem 2rem;
        border-radius: 25px;
        color: white;
        text-align: center;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><polygon fill="rgba(255,255,255,0.05)" points="0,1000 1000,0 1000,1000"/></svg>');
        background-size: cover;
    }
    
    /* Contact form */
    .contact-form {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 25px 25px 0 0;
        margin-top: 4rem;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="modern-header">
    <div class="nav-container">
        <div style="display: flex; align-items: center;">
            <h2 style="margin: 0; color: #667eea;">🏠 Green Vision</h2>
        </div>
        <div class="nav-links">
            <a href="#home" class="nav-link">Home</a>
            <a href="#services" class="nav-link">Services</a>
            <a href="#areas" class="nav-link">Areas</a>
            <a href="#process" class="nav-link">Process</a>
            <a href="#testimonials" class="nav-link">Reviews</a>
            <a href="#contact" class="nav-link">Contact</a>
        </div>
        <a href="https://www.propertyinspectionforimmigration.co.uk/contact" class="gradient-btn" style="text-decoration: none;">Get Quote</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section" id="home">
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
        <a href="https://www.propertyinspectionforimmigration.co.uk/contact" class="gradient-btn" style="background: white; color: #667eea; text-decoration: none;">Book Inspection Now</a>
        <a href="#services" class="outline-btn" style="border-color: white; color: white; text-decoration: none;">Learn More</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats Section
st.markdown("""
<div class="glass-card">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
        <div class="stat-card">
            <div class="stat-icon">🏠</div>
            <h3 style="font-size: 2.5rem; margin: 0; color: #667eea;">5000+</h3>
            <p style="color: #666; font-weight: 500;">Properties Inspected</p>
        </div>
        <div class="stat-card">
            <div class="stat-icon">⭐</div>
            <h3 style="font-size: 2.5rem; margin: 0; color: #667eea;">370+</h3>
            <p style="color: #666; font-weight: 500;">5-Star Reviews</p>
        </div>
        <div class="stat-card">
            <div class="stat-icon">✅</div>
            <h3 style="font-size: 2.5rem; margin: 0; color: #667eea;">100%</h3>
            <p style="color: #666; font-weight: 500;">Success Rate</p>
        </div>
        <div class="stat-card">
            <div class="stat-icon">⚡</div>
            <h3 style="font-size: 2.5rem; margin: 0; color: #667eea;">24h</h3>
            <p style="color: #666; font-weight: 500;">Fast Turnaround</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Services Section
st.markdown("""
<div class="section-header" id="services">
    <h2 class="section-title">Our Inspection Services</h2>
    <p style="font-size: 1.2rem; color: #666; max-width: 700px; margin: 0 auto;">Professional property inspection reports for all UK visa applications</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 3rem; color: #667eea; margin-bottom: 1rem;">📋</div>
        <h3 style="color: #333; margin-bottom: 1rem;">Spouse Visa Inspection</h3>
        <p style="color: #666; margin-bottom: 1.5rem;">Comprehensive property inspection reports specifically for spouse visa applications, meeting all UKVI requirements.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-spouse-visa/" class="gradient-btn" style="text-decoration: none; padding: 10px 20px; font-size: 0.9rem;">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 3rem; color: #667eea; margin-bottom: 1rem;">👨‍👩‍👧‍👦</div>
        <h3 style="color: #333; margin-bottom: 1rem;">Family Visa Inspection</h3>
        <p style="color: #666; margin-bottom: 1.5rem;">Property assessments for family visa applications ensuring your accommodation meets UK housing standards.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-family-visa-uk/" class="gradient-btn" style="text-decoration: none; padding: 10px 20px; font-size: 0.9rem;">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 3rem; color: #667eea; margin-bottom: 1rem;">⏰</div>
        <h3 style="color: #333; margin-bottom: 1rem;">24-Hour Emergency Service</h3>
        <p style="color: #666; margin-bottom: 1.5rem;">Need an urgent inspection? We offer 24-hour notice property inspections with fast report delivery.</p>
        <a href="https://www.propertyinspectionforimmigration.co.uk/contact" class="gradient-btn" style="text-decoration: none; padding: 10px 20px; font-size: 0.9rem;">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

# Areas Covered
st.markdown("""
<div class="section-header" id="areas">
    <h2 class="section-title">Areas We Cover</h2>
    <p style="font-size: 1.2rem; color: #666; max-width: 700px; margin: 0 auto;">We provide Property Inspection Reports throughout the UK</p>
</div>
""", unsafe_allow_html=True)

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

# Create a grid of area cards
cols = st.columns(4)
for i, area in enumerate(areas):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.08); margin-bottom: 1rem; transition: transform 0.3s ease;">
            <div style="font-size: 2rem; color: #667eea; margin-bottom: 0.5rem;">📍</div>
            <h4 style="margin: 0 0 0.5rem 0; color: #333;">{area['name']}</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">{area['description']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-top: 2rem;">
    <a href="https://www.propertyinspectionforimmigration.co.uk/areas-covered" class="gradient-btn" style="text-decoration: none;">View All Areas</a>
</div>
""", unsafe_allow_html=True)

# Process Section
st.markdown("""
<div class="section-header" id="process">
    <h2 class="section-title">Our Simple Process</h2>
    <p style="font-size: 1.2rem; color: #666; max-width: 700px; margin: 0 auto;">Get your Property Inspection Report in 3 easy steps</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 700; margin: 0 auto 1.5rem; box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);">1</div>
        <h3 style="color: #333; margin-bottom: 1rem;">Contact Us</h3>
        <p style="color: #666;">Call us or book online to schedule your property inspection at your convenience.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 700; margin: 0 auto 1.5rem; box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);">2</div>
        <h3 style="color: #333; margin-bottom: 1rem;">Property Visit</h3>
        <p style="color: #666;">Our certified surveyor visits your property within 24 hours to conduct a thorough inspection.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 700; margin: 0 auto 1.5rem; box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);">3</div>
        <h3 style="color: #333; margin-bottom: 1rem;">Receive Report</h3>
        <p style="color: #666;">Get your professional Property Inspection Report within 2 working days of the inspection.</p>
    </div>
    """, unsafe_allow_html=True)

# Testimonials
st.markdown("""
<div class="section-header" id="testimonials">
    <h2 class="section-title">Client Testimonials</h2>
    <p style="font-size: 1.2rem; color: #666; max-width: 700px; margin: 0 auto;">Over 370 five-star reviews from satisfied customers</p>
</div>
""", unsafe_allow_html=True)

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
            <p style="font-style: italic; color: #555; margin-bottom: 1.5rem;">"{testimonial['text']}"</p>
            <div style="display: flex; align-items: center;">
                <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; margin-right: 1rem;">
                    {testimonial['author'][0]}
                </div>
                <div>
                    <h4 style="margin: 0; color: #333;">{testimonial['author']}</h4>
                    <p style="margin: 0; color: #666; font-size: 0.9rem;">{testimonial['source']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# FAQ Section
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Frequently Asked Questions</h2>
    <p style="font-size: 1.2rem; color: #666; max-width: 700px; margin: 0 auto;">Find answers to common questions about our Property Inspection Reports</p>
</div>
""", unsafe_allow_html=True)

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
    <a href="https://www.propertyinspectionforimmigration.co.uk/frequently-asked-questions/" class="gradient-btn" style="text-decoration: none;">View All FAQs</a>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="section-header" id="contact">
    <h2 class="section-title">Contact Us</h2>
    <p style="font-size: 1.2rem; color: #666; max-width: 700px; margin: 0 auto;">Get in touch for a fast Property Inspection Report</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class="contact-form">
        <h3 style="color: #333; margin-bottom: 1.5rem;">Book an Inspection</h3>
        <form>
            <div style="margin-bottom: 1.5rem;">
                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500; color: #333;">Your Name</label>
                <input type="text" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 10px; font-family: 'Poppins', sans-serif;">
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500; color: #333;">Your Email</label>
                <input type="email" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 10px; font-family: 'Poppins', sans-serif;">
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500; color: #333;">Phone Number</label>
                <input type="tel" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 10px; font-family: 'Poppins', sans-serif;">
            </div>
            
            <div style="margin-bottom: 2rem;">
                <label style="display: block; margin-bottom: 0.5rem; font-weight: 500; color: #333;">Your Message</label>
                <textarea style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 10px; font-family: 'Poppins', sans-serif; height: 120px;" placeholder="Tell us about your property inspection needs..."></textarea>
            </div>
            
            <button type="submit" class="gradient-btn" style="width: 100%; padding: 15px; font-size: 1.1rem;">Send Message</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #333; margin-bottom: 1.5rem;">Get in Touch</h3>
        <p style="color: #666; margin-bottom: 2rem;">For reliable Property Inspection Reports in London and across the UK, contact Green Vision Engineers today.</p>
        
        <div style="margin-bottom: 2rem;">
            <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                <div style="font-size: 1.5rem; color: #667eea; margin-right: 1rem;">📞</div>
                <div>
                    <h4 style="margin: 0; color: #333;">Phone</h4>
                    <p style="margin: 0; color: #666;">Mobile: 07912 351 329</p>
                    <p style="margin: 0; color: #666;">Office: 020 3488 4930</p>
                </div>
            </div>
            
            <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                <div style="font-size: 1.5rem; color: #667eea; margin-right: 1rem;">✉️</div>
                <div>
                    <h4 style="margin: 0; color: #333;">Email</h4>
                    <p style="margin: 0; color: #666;">info@propertyinspectionforimmigration.co.uk</p>
                </div>
            </div>
            
            <div style="display: flex; align-items: center; margin-bottom: 2rem;">
                <div style="font-size: 1.5rem; color: #667eea; margin-right: 1rem;">📍</div>
                <div>
                    <h4 style="margin: 0; color: #333;">Office Address</h4>
                    <p style="margin: 0; color: #666;">241A Whitechapel Rd, London E1 1DB, United Kingdom</p>
                </div>
            </div>
        </div>
        
        <div style="border-radius: 15px; overflow: hidden; margin-bottom: 1rem;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3219.72147039414!2d-0.06103699999999998!3d51.51914529999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48761ccdc867bd5f%3A0x433ee054e9fa1361!2sProperty%20Inspection%20Report%20for%20UK%20Visa%20and%20Immigration!5e1!3m2!1sen!2suk!4v1759083676101!5m2!1sen!2suk" width="100%" height="200" style="border:0; border-radius: 10px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <a href="https://www.google.com/maps?cid=4845556904404587361" target="_blank" style="color: #667eea; font-weight: 600; text-decoration: none;">View on Google Maps ↗</a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 3rem; margin-bottom: 3rem;">
        <div>
            <h3 style="color: white; margin-bottom: 1.5rem;">Green Vision Engineers</h3>
            <p style="color: #bdc3c7; line-height: 1.6;">Leading provider of Property Inspection Reports for UK visa applications with over 12 years of experience.</p>
            <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
                <a href="https://en-gb.facebook.com/gvecuk/" style="color: white; text-decoration: none; background: rgba(255,255,255,0.1); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">f</a>
                <a href="#" style="color: white; text-decoration: none; background: rgba(255,255,255,0.1); width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">t</a>
            </div>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1.5rem;">Quick Links</h4>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">Home</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/our-surveyors/" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">Services</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/areas-covered" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">Areas Covered</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/about-us" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">About Us</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/contact" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">Contact Us</a></p>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1.5rem;">Our Services</h4>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/services" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">Spouse Visa Inspection</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/property-inspection-for-family-visa-uk/" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">Family Visa Inspection</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/contact" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">24-Hour Emergency Service</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">Property Inspection Report London</a></p>
            <p><a href="https://www.propertyinspectionforimmigration.co.uk/areas-covered" style="color: #bdc3c7; text-decoration: none; display: block; margin-bottom: 0.5rem;">Nationwide Coverage</a></p>
        </div>
        
        <div>
            <h4 style="color: white; margin-bottom: 1.5rem;">Contact Info</h4>
            <p style="color: #bdc3c7; margin-bottom: 0.5rem;">📞 07912 351 329</p>
            <p style="color: #bdc3c7; margin-bottom: 0.5rem;">📞 020 3488 4930</p>
            <p style="color: #bdc3c7; margin-bottom: 0.5rem;">✉️ info@propertyinspectionforimmigration.co.uk</p>
            <p style="color: #bdc3c7;">📍 241A Whitechapel Rd, London E1 1DB</p>
        </div>
    </div>
    
    <div style="text-align: center; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1);">
        <p style="color: #95a5a6; margin: 0;">© 2025 Property Inspection Report - All Rights Reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)
