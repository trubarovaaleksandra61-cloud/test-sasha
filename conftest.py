import pytest
from certificate_generator import CertificateGenerator


def pytest_configure(config):
    """Configure pytest hooks"""
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )


def pytest_sessionfinish(session, exitstatus):
    """Generate certificate after all tests complete"""
    if exitstatus == 0:  # All tests passed
        print("\n" + "="*80)
        print("🎉 ALL TESTS PASSED! Generating completion certificate...")
        print("="*80)
        
        generator = CertificateGenerator(
            user_name="Sasha Trubarova",
            test_count=20
        )
        
        # Generate all certificate formats
        generator.generate_html_certificate()
        generator.generate_json_certificate()
        generator.generate_text_certificate()
        
        print("\n" + "="*80)
        print("✓ Certificates generated successfully!")
        print("✓ Check: certificate.html, certificate.json, certificate.txt")
        print("="*80 + "\n")
    else:
        print("\n⚠️  Some tests failed. Certificate not generated.")
