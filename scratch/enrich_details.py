
import json

manifest_path = '/Users/pondokit/Herd/muhdanfyan.github.io/data/manifest.json'

with open(manifest_path, 'r') as f:
    data = json.load(f)

portfolio = data.get('portfolio', [])

for project in portfolio:
    slug = project.get('slug')
    
    if slug == 'mpad':
        project['process'] = "Pengembangan menggunakan Agile Scrum dengan siklus sprint 2 mingguan. Arsitektur dirancang dengan pola Driver-Based untuk menangani variasi protokol bank (H2H) secara modular. Implementasi mencakup middleware keamanan HMAC-SHA256 dan sistem caching Redis untuk performa inquiry tinggi."
        project['process_en'] = "Developed using Agile Scrum with 2-week sprint cycles. The architecture is designed with a Driver-Based pattern to handle bank protocol variations (H2H) modularly. Implementation includes HMAC-SHA256 security middleware and Redis caching for high inquiry performance."
        project['highlights'] = [
            "Arsitektur Driver-Based (Scalable)",
            "Keamanan HMAC-SHA256 & JIT Calculation",
            "Integrasi Domain Pemerintahan (.go.id)",
            "Workflow DevOps dengan Expect Scripts"
        ]
        project['highlights_en'] = [
            "Driver-Based Architecture (Scalable)",
            "HMAC-SHA256 & JIT Calculation Security",
            "Government Domain Integration (.go.id)",
            "DevOps Workflow with Expect Scripts"
        ]
        project['metrics'] = {
            "reliability": 99.9,
            "security": 100,
            "integration_speed": "300% Faster"
        }

    if slug == 'retribusi-admin':
        project['process'] = "Implementasi workflow Kanban yang ketat menggunakan GitHub Projects. Sistem dibangun dengan arsitektur micro-service-ready, memisahkan Admin Dashboard, API Core, dan Mobile App petugas. Menggunakan automated milestones dan sprint management."
        project['process_en'] = "Implementation of strict Kanban workflow using GitHub Projects. The system is built with micro-service-ready architecture, separating Admin Dashboard, API Core, and Officer Mobile App. Utilizing automated milestones and sprint management."
        project['highlights'] = [
            "Professional Kanban/Scrum Workflow",
            "Sistem Terintegrasi (Admin, API, Mobile)",
            "Automated Sprint Reporting",
            "Technical Documentation Lengkap"
        ]
        project['highlights_en'] = [
            "Professional Kanban/Scrum Workflow",
            "Integrated System (Admin, API, Mobile)",
            "Automated Sprint Reporting",
            "Complete Technical Documentation"
        ]

with open(manifest_path, 'w') as f:
    json.dump(data, f, indent=2)

print("Manifest enrichment completed.")
