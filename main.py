from flask import Flask, jsonify, render_template
from flask_cors import CORS
from datetime import datetime, timedelta
import random
import json

app = Flask(__name__)
CORS(app)

# ============================
# DATA DUMMY RUMAH SAKIT (KHUSUS BANDUNG)
# ============================
HOSPITALS = HOSPITALS = [
    {
        "id": "RS001", 
        "name": "RSUP Dr. Hasan Sadikin Bandung", 
        "type": "Tipe A",
        "address": "Jl. Pasteur No.38, Pasteur, Kec. Sukajadi, Kota Bandung"
    },
    {
        "id": "RS002", 
        "name": "RSUD Kota Bandung", 
        "type": "Tipe A",
        "address": "Jl. Rumah Sakit No.22, Cicendo, Kec. Bandung Kidul, Kota Bandung"
    },
    {
        "id": "RS003", 
        "name": "RS Advent Bandung", 
        "type": "Tipe B",
        "address": "Jl. Cihampelas No.161, Cipaganti, Kec. Coblong, Kota Bandung"
    },
    {
        "id": "RS004", 
        "name": "RS Santo Borromeus Bandung", 
        "type": "Tipe B",
        "address": "Jl. Ir. H. Juanda No.100, Lebakgede, Kec. Coblong, Kota Bandung"
    },
    {
        "id": "RS005", 
        "name": "RS Al Islam Bandung", 
        "type": "Tipe B",
        "address": "Jl. Soekarno Hatta No.644, Cipagalo, Kec. Bojongsoang, Kab. Bandung"
    },
    {
        "id": "RS006", 
        "name": "RSUD Ujung Berung", 
        "type": "Tipe C",
        "address": "Jl. AH Nasution No.50, Ujungberung, Kec. Ujung Berung, Kota Bandung"
    },
    {
        "id": "RS007", 
        "name": "RSIA Limijati Bandung", 
        "type": "Tipe C",
        "address": "Jl. Soekarno Hatta No.467, Sekejati, Kec. Buahbatu, Kota Bandung"
    },
    {
        "id": "RS008", 
        "name": "RS Khusus Paru Rotinsulu Bandung", 
        "type": "Tipe C",
        "address": "Jl. Buah Batu No.29, Turangga, Kec. Lengkong, Kota Bandung"
    },
]

def generate_bed_capacity():
    """Generate data kapasitas tempat tidur untuk semua RS"""
    data = []
    for hospital in HOSPITALS:
        icu_total = random.randint(20, 50)
        icu_occupied = random.randint(10, icu_total)
        regular_total = random.randint(100, 300)
        regular_occupied = random.randint(50, regular_total)
        isolation_total = random.randint(15, 40)
        isolation_occupied = random.randint(5, isolation_total)

        data.append({
            "hospital_id": hospital["id"],
            "hospital_name": hospital["name"],
            "icu": {
                "total": icu_total,
                "occupied": icu_occupied,
                "available": icu_total - icu_occupied,
                "occupancy_rate": round((icu_occupied / icu_total) * 100, 1)
            },
            "regular": {
                "total": regular_total,
                "occupied": regular_occupied,
                "available": regular_total - regular_occupied,
                "occupancy_rate": round((regular_occupied / regular_total) * 100, 1)
            },
            "isolation": {
                "total": isolation_total,
                "occupied": isolation_occupied,
                "available": isolation_total - isolation_occupied,
                "occupancy_rate": round((isolation_occupied / isolation_total) * 100, 1)
            },
            "last_updated": datetime.now().isoformat()
        })
    return data

def generate_er_status():
    """Generate data status IGD"""
    data = []
    for hospital in HOSPITALS:
        waiting = random.randint(5, 30)
        in_treatment = random.randint(10, 25)

        data.append({
            "hospital_id": hospital["id"],
            "hospital_name": hospital["name"],
            "waiting_patients": waiting,
            "in_treatment": in_treatment,
            "avg_waiting_time": random.randint(15, 90),
            "severity_distribution": {
                "critical": random.randint(1, 5),
                "urgent": random.randint(3, 10),
                "semi_urgent": random.randint(5, 15),
                "non_urgent": random.randint(2, 8)
            },
            "status": "normal" if waiting < 20 else "crowded",
            "last_updated": datetime.now().isoformat()
        })
    return data

def generate_queue_data():
    """Generate data antrian poliklinik"""
    polyclinics = ["Poli Umum", "Poli Anak", "Poli Gigi", "Poli Jantung", "Poli Paru"]
    data = []

    for hospital in HOSPITALS:
        for poly in polyclinics:
            current_queue = random.randint(0, 15)
            served_today = random.randint(20, 80)

            data.append({
                "hospital_id": hospital["id"],
                "hospital_name": hospital["name"],
                "polyclinic": poly,
                "current_queue": current_queue,
                "served_today": served_today,
                "avg_service_time": random.randint(10, 25),
                "estimated_wait": current_queue * random.randint(10, 20),
                "last_updated": datetime.now().isoformat()
            })
    return data

def generate_operational_metrics():
    """Generate KPI operasional harian"""
    data = []
    for hospital in HOSPITALS:
        data.append({
            "hospital_id": hospital["id"],
            "hospital_name": hospital["name"],
            "date": datetime.now().date().isoformat(),
            "metrics": {
                "total_admissions": random.randint(50, 150),
                "total_discharges": random.randint(40, 140),
                "er_visits": random.randint(80, 200),
                "outpatient_visits": random.randint(200, 500),
                "surgeries_completed": random.randint(5, 20),
                "lab_tests": random.randint(150, 400),
                "radiology_exams": random.randint(50, 150),
                "bed_turnover_rate": round(random.uniform(1.2, 2.5), 2),
                "avg_length_of_stay": round(random.uniform(3.5, 7.2), 1)
            },
            "last_updated": datetime.now().isoformat()
        })
    return data

def generate_staff_availability():
    """Generate data ketersediaan tenaga medis"""
    data = []
    for hospital in HOSPITALS:
        data.append({
            "hospital_id": hospital["id"],
            "hospital_name": hospital["name"],
            "staff": {
                "doctors": {
                    "on_duty": random.randint(15, 40),
                    "total": random.randint(50, 100),
                    "specialists_available": random.randint(8, 20)
                },
                "nurses": {
                    "on_duty": random.randint(50, 120),
                    "total": random.randint(150, 300)
                },
                "pharmacists": {
                    "on_duty": random.randint(5, 15),
                    "total": random.randint(15, 30)
                },
                "lab_technicians": {
                    "on_duty": random.randint(8, 20),
                    "total": random.randint(20, 40)
                }
            },
            "shift": "pagi" if datetime.now().hour < 15 else "sore",
            "last_updated": datetime.now().isoformat()
        })
    return data

def generate_resource_status():
    """Generate status ketersediaan sumber daya"""
    data = []
    for hospital in HOSPITALS:
        data.append({
            "hospital_id": hospital["id"],
            "hospital_name": hospital["name"],
            "resources": {
                "oxygen": {
                    "status": random.choice(["sufficient", "low", "critical"]),
                    "percentage": random.randint(40, 100)
                },
                "blood_bank": {
                    "A": random.randint(10, 50),
                    "B": random.randint(10, 50),
                    "AB": random.randint(5, 30),
                    "O": random.randint(15, 60)
                },
                "medical_supplies": {
                    "status": random.choice(["sufficient", "adequate", "low"]),
                    "critical_items": random.randint(0, 5)
                },
                "equipment": {
                    "ventilators_available": random.randint(5, 15),
                    "ventilators_total": random.randint(15, 25),
                    "ambulances_available": random.randint(3, 8),
                    "ambulances_total": random.randint(8, 12)
                }
            },
            "last_updated": datetime.now().isoformat()
        })
    return data

def generate_trend_data():
    """Generate data trend 7 hari terakhir"""
    dates = [(datetime.now() - timedelta(days=i)).date().isoformat() for i in range(6, -1, -1)]
    return {
        "dates": dates,
        "occupancy_trend": [random.randint(60, 90) for _ in range(7)],
        "er_visits_trend": [random.randint(100, 200) for _ in range(7)],
        "admissions_trend": [random.randint(50, 120) for _ in range(7)]
    }

@app.route('/')
def index():
    return render_template('index.html')

def generate_heatmap_data():
    """Generate data heatmap jam sibuk IGD per RS"""
    hours = list(range(24))  # 0-23 jam
    data = []
    
    for hospital in HOSPITALS:
        hourly_patients = []
        for hour in hours:
            # Simulasi pola: sibuk di pagi (7-11) dan sore (15-20)
            if 7 <= hour <= 11:
                base = random.randint(15, 35)
            elif 15 <= hour <= 20:
                base = random.randint(20, 40)
            elif 0 <= hour <= 5:
                base = random.randint(5, 15)
            else:
                base = random.randint(10, 25)
            
            hourly_patients.append(base)
        
        data.append({
            "hospital_id": hospital["id"],
            "hospital_name": hospital["name"],
            "hourly_data": hourly_patients
        })
    
    return data

@app.route('/api/visualizations')
def visualizations():
    """Endpoint untuk data visualisasi tambahan"""
    bed_data = generate_bed_capacity()
    metrics_data = generate_operational_metrics()
    
    # Data untuk diagram batang - perbandingan kunjungan per RS
    visits_comparison = []
    for metric in metrics_data:
        visits_comparison.append({
            "hospital": metric["hospital_name"],
            "er_visits": metric["metrics"]["er_visits"],
            "outpatient": metric["metrics"]["outpatient_visits"],
            "admissions": metric["metrics"]["total_admissions"]
        })
    
    # Data untuk diagram lingkaran - distribusi tipe tempat tidur
    total_icu = sum(h["icu"]["total"] for h in bed_data)
    total_regular = sum(h["regular"]["total"] for h in bed_data)
    total_isolation = sum(h["isolation"]["total"] for h in bed_data)
    
    bed_distribution = {
        "ICU": total_icu,
        "Reguler": total_regular,
        "Isolasi": total_isolation
    }
    
    # Data untuk diagram lingkaran - okupansi per RS
    occupancy_by_hospital = []
    heatmap_data = generate_heatmap_data()
    for h in bed_data:
        total = h["icu"]["total"] + h["regular"]["total"] + h["isolation"]["total"]
        occupied = h["icu"]["occupied"] + h["regular"]["occupied"] + h["isolation"]["occupied"]
        occupancy_by_hospital.append({
            "hospital": h["hospital_name"],
            "occupancy_rate": round((occupied / total) * 100, 1)
        })
    
    return jsonify({
        "visits_comparison": visits_comparison,
        "bed_distribution": bed_distribution,
        "occupancy_by_hospital": occupancy_by_hospital,
         "heatmap_data": heatmap_data,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/overview')
def overview():
    bed_data = generate_bed_capacity()
    er_data = generate_er_status()

    total_beds = sum(
        h["regular"]["total"] + h["icu"]["total"] + h["isolation"]["total"]
        for h in bed_data
    )
    occupied_beds = sum(
        h["regular"]["occupied"] + h["icu"]["occupied"] + h["isolation"]["occupied"]
        for h in bed_data
    )
    total_er_patients = sum(h["waiting_patients"] + h["in_treatment"] for h in er_data)

    return jsonify({
        "summary": {
            "total_hospitals": len(HOSPITALS),
            "total_beds": total_beds,
            "occupied_beds": occupied_beds,
            "available_beds": total_beds - occupied_beds,
            "occupancy_rate": round((occupied_beds / total_beds) * 100, 1),
            "total_er_patients": total_er_patients
        },
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/beds')
def beds():
    return jsonify({"data": generate_bed_capacity(), "timestamp": datetime.now().isoformat()})

@app.route('/api/emergency')
def emergency():
    return jsonify({"data": generate_er_status(), "timestamp": datetime.now().isoformat()})

@app.route('/api/queues')
def queues():
    return jsonify({"data": generate_queue_data(), "timestamp": datetime.now().isoformat()})

@app.route('/api/metrics')
def metrics():
    return jsonify({"data": generate_operational_metrics(), "timestamp": datetime.now().isoformat()})

@app.route('/api/staff')
def staff():
    return jsonify({"data": generate_staff_availability(), "timestamp": datetime.now().isoformat()})

@app.route('/api/resources')
def resources():
    return jsonify({"data": generate_resource_status(), "timestamp": datetime.now().isoformat()})

@app.route('/api/trends')
def trends():
    return jsonify({"data": generate_trend_data(), "timestamp": datetime.now().isoformat()})

@app.route('/api/hospitals')
def hospitals():
    return jsonify({"data": HOSPITALS, "timestamp": datetime.now().isoformat()})

def analyze_severity(complaint):
    """Analisis tingkat kegawatan berdasarkan keluhan"""
    complaint_lower = complaint.lower()
    
    # Keywords untuk critical
    critical_keywords = [
        'sesak', 'napas', 'dada sakit', 'nyeri dada', 'pingsan', 
        'tidak sadar', 'kejang', 'darah muntah', 'stroke', 
        'jantung', 'serangan jantung', 'kecelakaan', 'luka parah',
        'pendarahan hebat', 'trauma kepala', 'koma'
    ]
    
    # Keywords untuk urgent
    urgent_keywords = [
        'demam tinggi', 'muntah terus', 'diare parah', 'nyeri perut',
        'sakit perut hebat', 'luka bakar', 'patah tulang', 'cedera',
        'alergi parah', 'sesak ringan', 'pusing hebat', 'keracunan'
    ]
    
    # Keywords untuk semi-urgent
    semi_urgent_keywords = [
        'demam', 'batuk', 'flu', 'sakit kepala', 'mual', 'muntah',
        'diare', 'nyeri', 'bengkak', 'luka', 'infeksi', 'gatal'
    ]
    
    # Check severity
    for keyword in critical_keywords:
        if keyword in complaint_lower:
            return 'critical', 'Critical'
    
    for keyword in urgent_keywords:
        if keyword in complaint_lower:
            return 'urgent', 'Urgent'
    
    for keyword in semi_urgent_keywords:
        if keyword in complaint_lower:
            return 'semi_urgent', 'Semi-Urgent'
    
    return 'non_urgent', 'Non-Urgent'

@app.route('/api/referral/recommend', methods=['POST'])
def recommend_referral():
    """Endpoint untuk rekomendasi rujukan berdasarkan kondisi pasien"""
    from flask import request
    
    data = request.get_json()
    patient_name = data.get('name', '')
    patient_age = data.get('age', 0)
    complaint = data.get('complaint', '')
    specialty_needed = data.get('specialty', 'Umum')
    
    # Analisis kegawatan otomatis dari keluhan
    severity_code, severity_text = analyze_severity(complaint)
    
    # Get current data
    bed_data = generate_bed_capacity()
    er_data = generate_er_status()
    staff_data = generate_staff_availability()
    heatmap_data = generate_heatmap_data()
    
    current_hour = datetime.now().hour
    
    # Scoring system untuk rekomendasi
    recommendations = []
    
    for i, hospital in enumerate(HOSPITALS):
        bed_info = bed_data[i]
        er_info = er_data[i]
        staff_info = staff_data[i]
        hourly_traffic = heatmap_data[i]['hourly_data'][current_hour]
        
        # Calculate score (0-100)
        score = 0
        reasons = []
        
        # 1. Bed availability (30 points)
        bed_availability = bed_info['regular']['available'] + bed_info['icu']['available']
        if bed_availability > 50:
            score += 30
            reasons.append(f"Tempat tidur tersedia: {bed_availability}")
        elif bed_availability > 20:
            score += 20
            reasons.append(f"Tempat tidur cukup: {bed_availability}")
        else:
            score += 10
            reasons.append(f"Tempat tidur terbatas: {bed_availability}")
        
        # 2. ER status (25 points)
        if er_info['status'] == 'normal':
            score += 25
            reasons.append("IGD tidak padat")
        else:
            score += 10
            reasons.append("IGD sedang padat")
        
        # 3. Staff availability (25 points)
        doctor_ratio = staff_info['staff']['doctors']['on_duty'] / staff_info['staff']['doctors']['total']
        if doctor_ratio > 0.5:
            score += 25
            reasons.append(f"Dokter tersedia: {staff_info['staff']['doctors']['on_duty']} orang")
        elif doctor_ratio > 0.3:
            score += 15
            reasons.append(f"Dokter cukup: {staff_info['staff']['doctors']['on_duty']} orang")
        else:
            score += 5
            reasons.append(f"Dokter terbatas: {staff_info['staff']['doctors']['on_duty']} orang")
        
        # 4. Traffic hour (20 points)
        if hourly_traffic < 15:
            score += 20
            reasons.append("Jam sepi")
        elif hourly_traffic < 25:
            score += 10
            reasons.append("Jam cukup sepi")
        else:
            score += 0  # Tidak dapat poin jika ramai
            reasons.append("Jam ramai")
        
        # Penalty for high occupancy
        total_beds = bed_info['regular']['total'] + bed_info['icu']['total']
        total_occupied = bed_info['regular']['occupied'] + bed_info['icu']['occupied']
        occupancy_rate = (total_occupied / total_beds) * 100
        
        if occupancy_rate > 85:
            score -= 10
            reasons.append("⚠️ Okupansi tinggi")
        
        recommendations.append({
            "hospital_id": hospital['id'],
            "hospital_name": hospital['name'],
            "hospital_type": hospital['type'],
            "address": hospital['address'],
            "score": round(score, 1),
            "priority": "Sangat Direkomendasikan" if score >= 80 else "Direkomendasikan" if score >= 60 else "Alternatif",
            "reasons": reasons,
            "details": {
                "beds_available": bed_availability,
                "er_waiting": er_info['waiting_patients'],
                "doctors_on_duty": staff_info['staff']['doctors']['on_duty'],
                "specialists_available": staff_info['staff']['doctors']['specialists_available'],
                "occupancy_rate": round(occupancy_rate, 1),
                "current_traffic": hourly_traffic,
                "estimated_wait_time": er_info['avg_waiting_time']
            }
        })
    
    # Sort by score
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    
    return jsonify({
        "patient": {
            "name": patient_name,
            "age": patient_age,
            "complaint": complaint,
            "specialty": specialty_needed,
            "severity_code": severity_code,
            "severity_text": severity_text
        },
        "recommendations": recommendations,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
