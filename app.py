import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="London Property Inspections | Professional Building Surveyors",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
def local_css():
    st.markdown("""
    <style>
    :root {
        --primary: #2563eb;
        --primary-dark: #1d4ed8;
        --secondary: #0f172a;
        --accent: #f59e0b;
        --light: #f8fafc;
        --gray: #64748b;
        --gray-light: #e2e8f0;
        --white: #ffffff;
        --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        --border-radius: 8px;
        --transition: all 0.3s ease;
    }
    
    .main {
        padding: 0;
    }
    
    .stApp {
        background-color: var(--white);
    }
    
    .hero-section {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.9) 0%, rgba(29, 78, 216, 0.9) 100%);
        padding: 100px 0;
        text-align: center;
        color: white;
        margin-bottom: 0;
    }
    
    .section {
        padding: 80px 0;
    }
    
    .section-light {
        background-color: var(--light);
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 60px;
    }
    
    .section-header h2 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 15px;
        color: var(--secondary);
    }
    
    .section-header p {
        font-size: 1.125rem;
        color: var(--gray);
        max-width: 700px;
        margin: 0 auto;
    }
    
    .service-card {
        background-color: var(--white);
        border-radius: var(--border-radius);
        padding: 40px 30px;
        text-align: center;
        box-shadow: var(--shadow);
        transition: var(--transition);
        height: 100%;
    }
    
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: var(--shadow-lg);
    }
    
    .service-icon {
        width: 70px;
        height: 70px;
        background-color: rgba(37, 99, 235, 0.1);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 25px;
    }
    
    .service-icon i {
        font-size: 1.8rem;
        color: var(--primary);
    }
    
    .service-card h3 {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    
    .service-card p {
        color: var(--gray);
        margin-bottom: 20px;
    }
    
    .testimonial-card {
        background-color: var(--white);
        border-radius: var(--border-radius);
        padding: 30px;
        box-shadow: var(--shadow);
        height: 100%;
    }
    
    .testimonial-content {
        margin-bottom: 20px;
        position: relative;
    }
    
    .testimonial-content:before {
        content: '"';
        font-size: 4rem;
        color: var(--gray-light);
        position: absolute;
        top: -20px;
        left: -10px;
        z-index: 1;
    }
    
    .testimonial-content p {
        position: relative;
        z-index: 2;
        font-style: italic;
        color: var(--secondary);
    }
    
    .testimonial-author {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .author-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: var(--gray-light);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .author-avatar i {
        font-size: 1.5rem;
        color: var(--gray);
    }
    
    .author-info h4 {
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .author-info p {
        font-size: 0.875rem;
        color: var(--gray);
    }
    
    .step-container {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        margin-top: 50px;
        position: relative;
    }
    
    .step-container:before {
        content: '';
        position: absolute;
        top: 40px;
        left: 0;
        right: 0;
        height: 2px;
        background-color: var(--gray-light);
        z-index: 1;
    }
    
    .step {
        text-align: center;
        position: relative;
        z-index: 2;
        flex: 1;
        min-width: 200px;
        padding: 0 15px;
    }
    
    .step-number {
        width: 80px;
        height: 80px;
        background-color: var(--primary);
        color: var(--white);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 auto 20px;
        position: relative;
    }
    
    .step h3 {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    
    .step p {
        color: var(--gray);
    }
    
    .contact-item {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 20px;
    }
    
    .contact-icon {
        width: 50px;
        height: 50px;
        background-color: rgba(37, 99, 235, 0.1);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .contact-icon i {
        font-size: 1.25rem;
        color: var(--primary);
    }
    
    .contact-text h4 {
        font-weight: 600;
        margin-bottom: 5px;
    }
    
    .contact-text p {
        color: var(--gray);
        margin: 0;
    }
    
    .footer {
        background-color: var(--secondary);
        color: var(--white);
        padding: 70px 0 30px;
    }
    
    .footer-col h3 {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 25px;
        position: relative;
    }
    
    .footer-col h3:after {
        content: '';
        position: absolute;
        left: 0;
        bottom: -10px;
        width: 40px;
        height: 2px;
        background-color: var(--primary);
    }
    
    .footer-col ul {
        list-style: none;
        padding: 0;
    }
    
    .footer-col ul li {
        margin-bottom: 12px;
    }
    
    .footer-col ul li a {
        color: rgba(255, 255, 255, 0.7);
        text-decoration: none;
        transition: var(--transition);
    }
    
    .footer-col ul li a:hover {
        color: var(--white);
        padding-left: 5px;
    }
    
    .social-links {
        display: flex;
        gap: 15px;
        margin-top: 20px;
    }
    
    .social-links a {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        color: var(--white);
        text-decoration: none;
        transition: var(--transition);
    }
    
    .social-links a:hover {
        background-color: var(--primary);
        transform: translateY(-3px);
    }
    
    .footer-bottom {
        text-align: center;
        padding-top: 30px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.875rem;
    }
    
    .cta-button {
        background-color: var(--primary);
        color: var(--white);
        border: none;
        padding: 12px 24px;
        border-radius: var(--border-radius);
        font-weight: 600;
        cursor: pointer;
        transition: var(--transition);
        text-decoration: none;
        display: inline-block;
    }
    
    .cta-button:hover {
        background-color: var(--primary-dark);
        transform: translateY(-2px);
    }
    
    .secondary-button {
        background-color: transparent;
        color: var(--white);
        border: 2px solid var(--white);
        padding: 12px 24px;
        border-radius: var(--border-radius);
        font-weight: 600;
        cursor: pointer;
        transition: var(--transition);
        text-decoration: none;
        display: inline-block;
    }
    
    .secondary-button:hover {
        background-color: var(--white);
        color: var(--primary);
    }
    
    @media (max-width: 768px) {
        .step-container:before {
            display: none;
        }
        
        .step {
            margin-bottom: 40px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for form
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# Hero Section
def hero_section():
    st.markdown("""
    <div class="hero-section">
        <div style="max-width: 800px; margin: 0 auto;">
            <h1 style="font-size: 3.5rem; font-weight: 700; margin-bottom: 20px; line-height: 1.2;">Professional Property Inspection Services in London</h1>
            <p style="font-size: 1.25rem; margin-bottom: 30px; opacity: 0.9;">Comprehensive building surveys and inspection reports to help you make informed property decisions with confidence.</p>
            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="#contact-form" style="background-color: white; color: #2563eb; border: none; padding: 12px 24px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; text-decoration: none; display: inline-block;">Get Your Quote</a>
                <a href="#services" style="background-color: transparent; color: white; border: 2px solid white; padding: 12px 24px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; text-decoration: none; display: inline-block;">Our Services</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Services Section
def services_section():
    st.markdown('<div class="section section-light" id="services">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-header">
        <h2>Our Inspection Services</h2>
        <p>We offer a range of professional property inspection services tailored to your specific needs.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">
                <i class="fas fa-clipboard-check">📋</i>
            </div>
            <h3>Home Buyer Report</h3>
            <p>Comprehensive inspection and report for prospective home buyers, identifying issues that may affect your decision.</p>
            <a href="#contact-form" class="cta-button">Learn More</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">
                <i class="fas fa-building">🏢</i>
            </div>
            <h3>Building Survey</h3>
            <p>Detailed structural assessment for older properties or those in need of renovation.</p>
            <a href="#contact-form" class="cta-button">Learn More</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="service-card">
            <div class="service-icon">
                <i class="fas fa-list-check">✅</i>
            </div>
            <h3>Snagging List</h3>
            <p>Thorough inspection of new build properties to identify defects before you complete your purchase.</p>
            <a href="#contact-form" class="cta-button">Learn More</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Process Section
def process_section():
    st.markdown('<div class="section" id="process">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-header">
        <h2>Our Simple Process</h2>
        <p>Getting a professional property inspection has never been easier with our straightforward process.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-container">
        <div class="step">
            <div class="step-number">1</div>
            <h3>Book Inspection</h3>
            <p>Contact us to schedule your property inspection at a convenient time.</p>
        </div>
        <div class="step">
            <div class="step-number">2</div>
            <h3>Property Assessment</h3>
            <p>Our certified surveyors conduct a thorough inspection of the property.</p>
        </div>
        <div class="step">
            <div class="step-number">3</div>
            <h3>Detailed Report</h3>
            <p>Receive a comprehensive report with findings and recommendations.</p>
        </div>
        <div class="step">
            <div class="step-number">4</div>
            <h3>Follow-up Support</h3>
            <p>We're available to answer any questions and provide further guidance.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Testimonials Section
def testimonials_section():
    st.markdown('<div class="section section-light" id="testimonials">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-header">
        <h2>What Our Clients Say</h2>
        <p>Don't just take our word for it - hear from our satisfied customers across London.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="testimonial-card">
            <div class="testimonial-content">
                <p>The inspection report was incredibly detailed and helped us negotiate a better price on our new home. The surveyor was professional and answered all our questions.</p>
            </div>
            <div class="testimonial-author">
                <div class="author-avatar">
                    <i class="fas fa-user">👤</i>
                </div>
                <div class="author-info">
                    <h4>Sarah Johnson</h4>
                    <p>Kensington</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="testimonial-card">
            <div class="testimonial-content">
                <p>As a first-time buyer, I was nervous about the process. The team made everything clear and the report highlighted issues I would never have spotted myself.</p>
            </div>
            <div class="testimonial-author">
                <div class="author-avatar">
                    <i class="fas fa-user">👤</i>
                </div>
                <div class="author-info">
                    <h4>Michael Chen</h4>
                    <p>Islington</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="testimonial-card">
            <div class="testimonial-content">
                <p>We've used London Property Inspections for three property purchases now. Their consistent quality and attention to detail give us complete confidence in our investments.</p>
            </div>
            <div class="testimonial-author">
                <div class="author-avatar">
                    <i class="fas fa-user">👤</i>
                </div>
                <div class="author-info">
                    <h4>Robert & Emma Wilson</h4>
                    <p>Greenwich</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# CTA Section
def cta_section():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: white; padding: 100px 0; text-align: center;">
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 style="font-size: 2.5rem; font-weight: 700; margin-bottom: 20px;">Ready to Protect Your Property Investment?</h2>
            <p style="font-size: 1.125rem; margin-bottom: 30px; opacity: 0.9; max-width: 700px; margin-left: auto; margin-right: auto;">Don't leave your property purchase to chance. Our expert inspectors will give you the confidence to proceed with your transaction.</p>
            <a href="#contact-form" style="background-color: white; color: #2563eb; border: none; padding: 12px 24px; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease; text-decoration: none; display: inline-block;">Schedule Your Inspection</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Contact Section
def contact_section():
    st.markdown('<div class="section" id="contact">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="padding-right: 40px;">
            <h2 style="font-size: 2.5rem; font-weight: 700; margin-bottom: 20px;">Get In Touch</h2>
            <p style="color: #64748b; margin-bottom: 30px;">Contact us today to schedule your property inspection or to learn more about our services.</p>
            
            <div class="contact-details">
                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-phone">📞</i>
                    </div>
                    <div class="contact-text">
                        <h4>Phone</h4>
                        <p>020 7123 4567</p>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-envelope">✉️</i>
                    </div>
                    <div class="contact-text">
                        <h4>Email</h4>
                        <p>info@londonpropertyinspections.co.uk</p>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-map-marker-alt">📍</i>
                    </div>
                    <div class="contact-text">
                        <h4>Office</h4>
                        <p>123 Inspection Lane, London, EC1A 1BB</p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div id="contact-form"></div>', unsafe_allow_html=True)
        st.markdown("### Request a Quote")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full Name", placeholder="Your Name")
            email = st.text_input("Email Address", placeholder="Your Email")
            phone = st.text_input("Phone Number", placeholder="Your Phone")
            service = st.selectbox(
                "Service Required",
                ["Select a Service", "Home Buyer Report", "Building Survey", "Snagging List", "Other"]
            )
            message = st.text_area("Message", placeholder="Tell us about your property...", height=120)
            
            submitted = st.form_submit_button("Send Message", type="primary")
            
            if submitted:
                if name and email and service != "Select a Service":
                    st.session_state.form_submitted = True
                    st.success("Thank you for your inquiry! We will contact you shortly.")
                else:
                    st.error("Please fill in all required fields.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
def footer():
    st.markdown("""
    <div class="footer">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; margin-bottom: 50px;">
                <div class="footer-col">
                    <h3>London Property Inspections</h3>
                    <p>Professional property inspection services across London, helping buyers make informed decisions with confidence.</p>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-facebook-f">f</i></a>
                        <a href="#"><i class="fab fa-twitter">t</i></a>
                        <a href="#"><i class="fab fa-linkedin-in">in</i></a>
                        <a href="#"><i class="fab fa-instagram">ig</i></a>
                    </div>
                </div>
                <div class="footer-col">
                    <h3>Our Services</h3>
                    <ul>
                        <li><a href="#">Home Buyer Reports</a></li>
                        <li><a href="#">Building Surveys</a></li>
                        <li><a href="#">Snagging Lists</a></li>
                        <li><a href="#">Commercial Inspections</a></li>
                        <li><a href="#">Damp & Timber Surveys</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="#services">Services</a></li>
                        <li><a href="#process">Our Process</a></li>
                        <li><a href="#testimonials">Testimonials</a></li>
                        <li><a href="#contact">Contact</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Contact Us</h3>
                    <ul>
                        <li>📞 020 7123 4567</li>
                        <li>✉️ info@londonpropertyinspections.co.uk</li>
                        <li>📍 123 Inspection Lane, London, EC1A 1BB</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2023 London Property Inspections. All rights reserved.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    # Apply custom CSS
    local_css()
    
    # Hide Streamlit default elements
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Navigation (simplified for Streamlit)
    st.markdown("""
    <div style="background-color: white; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); position: sticky; top: 0; z-index: 100; padding: 20px 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <a href="#" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: #0f172a; font-weight: 700; font-size: 1.5rem;">
                <span style="color: #2563eb; font-size: 1.8rem;">🏠</span>
                <span>London Property Inspections</span>
            </a>
            <div style="display: flex; gap: 30px;">
                <a href="#services" style="text-decoration: none; color: #0f172a; font-weight: 500;">Services</a>
                <a href="#process" style="text-decoration: none; color: #0f172a; font-weight: 500;">Process</a>
                <a href="#testimonials" style="text-decoration: none; color: #0f172a; font-weight: 500;">Testimonials</a>
                <a href="#contact" style="text-decoration: none; color: #0f172a; font-weight: 500;">Contact</a>
            </div>
            <a href="#contact-form" style="background-color: #2563eb; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-weight: 600; cursor: pointer; text-decoration: none;">Book Inspection</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Page sections
    hero_section()
    services_section()
    process_section()
    testimonials_section()
    cta_section()
    contact_section()
    footer()

if __name__ == "__main__":
    main()
