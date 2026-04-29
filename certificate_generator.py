from datetime import datetime
from pathlib import Path
import json


class CertificateGenerator:
    """Generate test completion certificate"""
    
    def __init__(self, user_name="Test Student", test_count=20):
        self.user_name = user_name
        self.test_count = test_count
        self.completion_date = datetime.now().strftime("%d.%m.%Y")
        self.completion_time = datetime.now().strftime("%H:%M:%S")
    
    def generate_html_certificate(self, output_file="certificate.html"):
        """Generate HTML certificate"""
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Completion Certificate</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Arial', sans-serif;
        }}
        .certificate {{
            width: 900px;
            height: 600px;
            background: linear-gradient(to bottom, #fff8f0, #fffef7);
            border: 8px solid #d4af37;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            padding: 60px;
            text-align: center;
            position: relative;
            border-radius: 10px;
        }}
        .certificate::before {{
            content: '';
            position: absolute;
            top: -8px;
            left: -8px;
            right: -8px;
            bottom: -8px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            z-index: -1;
            border-radius: 10px;
        }}
        .header {{
            color: #d4af37;
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 3px;
        }}
        .subtitle {{
            color: #764ba2;
            font-size: 20px;
            margin-bottom: 40px;
            font-style: italic;
        }}
        .content {{
            margin: 40px 0;
        }}
        .name {{
            font-size: 36px;
            color: #333;
            margin: 30px 0;
            font-weight: bold;
            text-decoration: underline;
        }}
        .achievement {{
            font-size: 16px;
            color: #555;
            margin: 20px 0;
            line-height: 1.8;
        }}
        .details {{
            display: flex;
            justify-content: space-around;
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #d4af37;
        }}
        .detail-item {{
            text-align: center;
        }}
        .detail-label {{
            font-size: 12px;
            color: #999;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .detail-value {{
            font-size: 16px;
            color: #333;
            font-weight: bold;
            margin-top: 5px;
        }}
        .badge {{
            display: inline-block;
            width: 80px;
            height: 80px;
            background: #d4af37;
            border-radius: 50%;
            margin: 30px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
        }}
    </style>
</head>
<body>
    <div class="certificate">
        <div class="badge">✓</div>
        <div class="header">Certificate of Completion</div>
        <div class="subtitle">This is to certify that</div>
        <div class="name">{self.user_name}</div>
        <div class="achievement">
            has successfully completed and passed all <strong>{self.test_count} tests</strong><br>
            demonstrating proficiency in Python programming and testing methodologies.
        </div>
        <div class="achievement">
            This certificate is awarded in recognition of outstanding achievement<br>
            and dedication to learning and development.
        </div>
        <div class="details">
            <div class="detail-item">
                <div class="detail-label">Tests Passed</div>
                <div class="detail-value">{self.test_count}/20</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Date</div>
                <div class="detail-value">{self.completion_date}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Time</div>
                <div class="detail-value">{self.completion_time}</div>
            </div>
        </div>
    </div>
</body>
</html>
        """
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ HTML certificate generated: {output_file}")
        return output_file
    
    def generate_json_certificate(self, output_file="certificate.json"):
        """Generate JSON certificate data"""
        certificate_data = {
            "certificate_type": "Test Completion",
            "student_name": self.user_name,
            "tests_completed": self.test_count,
            "tests_passed": self.test_count,
            "success_rate": "100%",
            "completion_date": self.completion_date,
            "completion_time": self.completion_time,
            "issued_at": datetime.now().isoformat(),
            "status": "CERTIFIED"
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(certificate_data, f, indent=4, ensure_ascii=False)
        
        print(f"✓ JSON certificate generated: {output_file}")
        return output_file
    
    def generate_text_certificate(self, output_file="certificate.txt"):
        """Generate text certificate"""
        text_content = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     CERTIFICATE OF COMPLETION                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

                            This is to certify that

                         ★ {self.user_name:^40} ★

                    has successfully completed and passed all

                              {self.test_count} PYTHON TESTS

            demonstrating proficiency in programming and testing skills.


╔══════════════════════════════════════════════════════════════════════════════╗
║ ACHIEVEMENT DETAILS                                                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Tests Completed: {self.test_count}/20                                       
║  Success Rate: 100%                                                         ║
║  Completion Date: {self.completion_date}                                       
║  Completion Time: {self.completion_time}                                       
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

        This certificate is awarded in recognition of outstanding
        achievement and dedication to learning and development.

                    Certificate ID: CERT-{datetime.now().strftime('%Y%m%d%H%M%S')}

"""
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text_content)
        
        print(f"✓ Text certificate generated: {output_file}")
        return output_file
