DISEASE_DATA = {

'TB': {
    'medicines_positive': [
        {'name': 'Isoniazid (INH)',   'use': 'First-line antibiotic — kills TB bacteria', 'type': 'Antibiotic'},
        {'name': 'Rifampicin',        'use': 'Kills TB bacteria, used in combination',    'type': 'Antibiotic'},
        {'name': 'Pyrazinamide',      'use': 'Shortens TB treatment duration',            'type': 'Antibiotic'},
        {'name': 'Ethambutol',        'use': 'Prevents drug resistance development',      'type': 'Antibiotic'},
    ],
    'tips_positive': [
        'Take all medications for the full 6-9 month course without stopping',
        'Cover your mouth with a tissue when coughing or sneezing',
        'Sleep in a well-ventilated room with fresh air circulation',
        'Eat a high-protein, nutritious diet to support immune recovery',
        'Avoid close contact with others especially in enclosed spaces',
        'Attend all follow-up sputum tests and chest X-rays as scheduled',
        'Do not share utensils, towels, or clothing with family members',
        'Report any side effects like yellowing of skin to your doctor immediately',
    ],
    'tips_negative': [
        'Get BCG vaccine if not already vaccinated',
        'Avoid overcrowded poorly ventilated places',
        'Maintain good nutrition and a strong immune system',
        'Get tested if you have a cough lasting more than 2 weeks',
        'Avoid contact with known TB patients without wearing a mask',
    ],
    'similar_diseases': [
        {
            'name': 'Pneumonia',
            'reason': 'Shares symptoms of persistent cough, fever, chest pain and fatigue. Unlike TB, pneumonia is acute and develops rapidly over days.',
            'difference': 'TB develops slowly over weeks or months. Pneumonia usually has sudden onset with higher fever and is not infectious in the same way.',
        },
        {
            'name': 'Chronic Bronchitis',
            'reason': 'Persistent cough, shortness of breath, and fatigue are common in both. Smokers are at higher risk.',
            'difference': 'TB involves night sweats, weight loss, and coughing blood which are not typical in bronchitis. TB requires sputum test confirmation.',
        },
       
    ],
  'hospitals': {
            'Delhi': [
                {'name': 'Rajan Babu TB Hospital', 'address': 'Kingsway Camp, Delhi', 'phone': '011-27667700', 'specialty': 'TB Specialist'},
                {'name': 'LRS Institute of TB', 'address': 'Mehrauli, New Delhi', 'phone': '011-26511747', 'specialty': 'Pulmonology'},
            ],
            'Maharashtra': [
                {'name': 'Sewri TB Hospital', 'address': 'Sewri, Mumbai', 'phone': '022-23770251', 'specialty': 'TB Specialist'},
                {'name': 'Wadia Hospital', 'address': 'Parel, Mumbai', 'phone': '022-24136051', 'specialty': 'Respiratory'},
            ],
            'Tamil Nadu': [
                {'name': 'Government Stanley Hospital', 'address': 'Stanley Road, Chennai', 'phone': '044-25281201', 'specialty': 'TB & Chest'},
                {'name': 'Government Chest Hospital', 'address': 'Egmore, Chennai', 'phone': '044-28193001', 'specialty': 'Pulmonology'},
            ],
            'Karnataka': [
                {'name': 'NIMHANS Hospital', 'address': 'Hosur Road, Bengaluru', 'phone': '080-46110007', 'specialty': 'General & TB'},
                {'name': 'Victoria Hospital', 'address': 'Fort Road, Bengaluru', 'phone': '080-26701150', 'specialty': 'TB Specialist'},
            ],
            'West Bengal': [
                {'name': 'Infectious Disease Hospital', 'address': 'Beliaghata, Kolkata', 'phone': '033-23231473', 'specialty': 'Infectious Disease'},
                {'name': 'SSKM Hospital', 'address': 'AJC Bose Road, Kolkata', 'phone': '033-22041739', 'specialty': 'Pulmonology'},
            ],
            'Uttar Pradesh': [
                {'name': 'KGMU Hospital', 'address': 'Chowk, Lucknow', 'phone': '0522-2257540', 'specialty': 'Chest & TB'},
                {'name': 'Ram Manohar Lohia Hospital', 'address': 'Lucknow', 'phone': '0522-2235944', 'specialty': 'General'},
            ],
            'Gujarat': [
                {'name': 'Civil Hospital Ahmedabad', 'address': 'Asarwa, Ahmedabad', 'phone': '079-22681234', 'specialty': 'TB Specialist'},
                {'name': 'Shardaben Hospital', 'address': 'Ahmedabad', 'phone': '079-25505050', 'specialty': 'Pulmonology'},
            ],
            'Rajasthan': [
                {'name': 'SMS Hospital', 'address': 'JLN Marg, Jaipur', 'phone': '0141-2518501', 'specialty': 'TB & Chest'},
                {'name': 'TB Hospital Jaipur', 'address': 'Jaipur', 'phone': '0141-2706251', 'specialty': 'TB Specialist'},
            ],
            'Kerala': [
                {'name': 'Government Medical College', 'address': 'Thiruvananthapuram', 'phone': '0471-2528386', 'specialty': 'Pulmonology'},
                {'name': 'Calicut Medical College', 'address': 'Kozhikode', 'phone': '0495-2350216', 'specialty': 'TB & Chest'},
            ],
            'Telangana': [
                {'name': 'Gandhi Hospital', 'address': 'Secunderabad, Hyderabad', 'phone': '040-27505566', 'specialty': 'General & TB'},
                {'name': 'Chest Hospital', 'address': 'Erragadda, Hyderabad', 'phone': '040-23810610', 'specialty': 'TB Specialist'},
            ],
        }
    },
'MAL': {
    'medicines_positive': [
        {'name': 'Chloroquine',             'use': 'First-line for P. vivax malaria',         'type': 'Antimalarial'},
        {'name': 'Artemether-Lumefantrine', 'use': 'For P. falciparum malaria',               'type': 'Antimalarial'},
        {'name': 'Primaquine',              'use': 'Clears liver-stage parasites',             'type': 'Antimalarial'},
        {'name': 'Paracetamol 500mg',       'use': 'Controls high fever and body ache',       'type': 'Antipyretic'},
    ],
    'tips_positive': [
        'Complete the full antimalarial course even if you feel better',
        'Stay well hydrated — drink at least 3 litres of water daily',
        'Use a mosquito net with insecticide treatment while sleeping',
        'Take complete rest — avoid any physical exertion',
        'Monitor for danger signs: seizures, confusion, difficulty breathing',
        'Take a blood smear test to confirm malaria species before treatment',
        'Avoid self-medication — wrong antimalarial can cause resistance',
        'Follow up with blood test after 3 days to check parasite clearance',
    ],
    'tips_negative': [
        'Use DEET-based insect repellent when going outdoors',
        'Sleep under insecticide-treated mosquito nets',
        'Eliminate all sources of stagnant water near your home',
        'Wear full-sleeve clothing during evening hours',
        'Take prophylactic medicines when travelling to endemic areas',
    ],
    'similar_diseases': [
        {
            'name': 'Dengue Fever',
            'reason': 'Both cause sudden high fever, severe headache, muscle and joint pain, and are transmitted by mosquitoes.',
            'difference': 'Dengue causes severe bone pain (breakbone fever), skin rash, and low platelet count. Malaria has cyclical fever pattern every 48-72 hours.',
        },
        {
            'name': 'Typhoid Fever',
            'reason': 'Both cause prolonged fever, headache, weakness, and loss of appetite that can last for weeks.',
            'difference': 'Typhoid causes a step-wise rising fever, rose-coloured spots on abdomen, and is confirmed by Widal test. Malaria is confirmed by blood smear.',
        },
        {
            'name': 'Chikungunya',
            'reason': 'Sudden onset fever, severe joint pain, headache and fatigue are shared symptoms.',
            'difference': 'Chikungunya causes intense joint swelling and pain that persists for months. Malaria has the characteristic cyclical fever which Chikungunya does not.',
        },
    ],
'hospitals': {
            'Delhi': [
                {'name': 'Safdarjung Hospital', 'address': 'Ansari Nagar, New Delhi', 'phone': '011-26707444', 'specialty': 'Infectious Disease'},
                {'name': 'AIIMS Delhi', 'address': 'Ansari Nagar, New Delhi', 'phone': '011-26588500', 'specialty': 'Tropical Medicine'},
            ],
            'Maharashtra': [
                {'name': 'KEM Hospital', 'address': 'Parel, Mumbai', 'phone': '022-24107000', 'specialty': 'Infectious Disease'},
                {'name': 'Nair Hospital', 'address': 'Mumbai Central', 'phone': '022-23027644', 'specialty': 'Tropical Medicine'},
            ],
            'Odisha': [
                {'name': 'SCB Medical College', 'address': 'Cuttack', 'phone': '0671-2414004', 'specialty': 'Malaria Specialist'},
                {'name': 'Capital Hospital', 'address': 'Bhubaneswar', 'phone': '0674-2392200', 'specialty': 'Infectious Disease'},
            ],
            'West Bengal': [
                {'name': 'School of Tropical Medicine', 'address': 'CR Avenue, Kolkata', 'phone': '033-22214141', 'specialty': 'Tropical Medicine'},
                {'name': 'Calcutta Medical College', 'address': 'College Street, Kolkata', 'phone': '033-22123208', 'specialty': 'Infectious Disease'},
            ],
            'Assam': [
                {'name': 'GMCH Gauhati', 'address': 'Bhangagarh, Guwahati', 'phone': '0361-2529457', 'specialty': 'Malaria Specialist'},
                {'name': 'Silchar Medical College', 'address': 'Silchar', 'phone': '03842-224729', 'specialty': 'Tropical Disease'},
            ],
            'Karnataka': [
                {'name': 'Bowring Hospital', 'address': 'Shivajinagar, Bengaluru', 'phone': '080-25561902', 'specialty': 'Infectious Disease'},
                {'name': 'Rajiv Gandhi Institute', 'address': 'Jayanagar, Bengaluru', 'phone': '080-26565050', 'specialty': 'General Medicine'},
            ],
            'Tamil Nadu': [
                {'name': 'Government General Hospital', 'address': 'Park Town, Chennai', 'phone': '044-25305000', 'specialty': 'Tropical Medicine'},
                {'name': 'Kilpauk Medical College', 'address': 'Kilpauk, Chennai', 'phone': '044-26421222', 'specialty': 'Infectious Disease'},
            ],
            'Gujarat': [
                {'name': 'Civil Hospital', 'address': 'Asarwa, Ahmedabad', 'phone': '079-22681234', 'specialty': 'Malaria Treatment'},
                {'name': 'VS Hospital', 'address': 'Ellisbridge, Ahmedabad', 'phone': '079-26578492', 'specialty': 'General Medicine'},
            ],
            'Rajasthan': [
                {'name': 'SMS Hospital', 'address': 'JLN Marg, Jaipur', 'phone': '0141-2518501', 'specialty': 'Infectious Disease'},
                {'name': 'JK Lon Hospital', 'address': 'Jaipur', 'phone': '0141-2706001', 'specialty': 'General Medicine'},
            ],
            'Kerala': [
                {'name': 'Kozhikode Medical College', 'address': 'Kozhikode', 'phone': '0495-2350216', 'specialty': 'Tropical Medicine'},
                {'name': 'Thrissur District Hospital', 'address': 'Thrissur', 'phone': '0487-2422211', 'specialty': 'General Medicine'},
            ],
        }
    },
'ASTH': {
    'medicines_positive': [
        {'name': 'Salbutamol Inhaler',   'use': 'Quick-relief bronchodilator for acute attacks', 'type': 'SABA Bronchodilator'},
        {'name': 'Budesonide Inhaler',   'use': 'Reduces airway inflammation long-term',         'type': 'Inhaled Corticosteroid'},
        {'name': 'Montelukast 10mg',     'use': 'Prevents symptoms and allergic reactions',      'type': 'Leukotriene Modifier'},
        {'name': 'Formoterol Inhaler',   'use': 'Long-acting bronchodilator for daily control',  'type': 'LABA Bronchodilator'},
    ],
    'tips_positive': [
        'Always carry your rescue inhaler (Salbutamol) wherever you go',
        'Identify and strictly avoid your personal asthma triggers',
        'Keep windows closed during high pollen and dust seasons',
        'Use air purifiers and vacuum regularly to reduce indoor allergens',
        'Practice pursed-lip breathing during mild breathlessness',
        'Monitor peak flow readings daily if your doctor has prescribed a meter',
        'Get annual flu vaccination as respiratory infections worsen asthma',
        'Never smoke and avoid second-hand smoke completely',
    ],
    'tips_negative': [
        'Avoid smoking and second-hand smoke completely',
        'Exercise regularly but warm up slowly before intense activity',
        'Keep your home free of dust mites, pet dander, and mold',
        'Avoid strong chemical fumes, perfumes, and sprays',
        'Get flu vaccination annually to protect respiratory health',
    ],
    'similar_diseases': [
        {
            'name': 'COPD (Chronic Obstructive Pulmonary Disease)',
            'reason': 'Both cause shortness of breath, chronic cough, and wheezing. Both are long-term respiratory conditions.',
            'difference': 'COPD is mostly caused by smoking and occurs in older adults. It is irreversible. Asthma is reversible, often starts in childhood, and is triggered by allergens.',
        },
        {
            'name': 'Allergic Rhinitis',
            'reason': 'Both are triggered by allergens, cause coughing, and breathing difficulty. Many patients have both together.',
            'difference': 'Allergic rhinitis primarily affects the nose — runny nose, sneezing, nasal congestion. Asthma affects the lower airways causing wheezing and chest tightness.',
        },
        {
            'name': 'Vocal Cord Dysfunction (VCD)',
            'reason': 'Causes sudden shortness of breath, wheezing-like sounds, and chest tightness very similar to asthma.',
            'difference': 'VCD does not respond to asthma inhalers. It is diagnosed by laryngoscopy and occurs during inspiration, while asthma wheezing occurs during expiration.',
        },
    ],
   'hospitals': {
            'Delhi': [
                {'name': 'AIIMS Respiratory Unit', 'address': 'Ansari Nagar, New Delhi', 'phone': '011-26588500', 'specialty': 'Pulmonology'},
                {'name': 'Sir Ganga Ram Hospital', 'address': 'Rajinder Nagar, Delhi', 'phone': '011-25750000', 'specialty': 'Respiratory Medicine'},
            ],
            'Maharashtra': [
                {'name': 'Bombay Hospital', 'address': 'Marine Lines, Mumbai', 'phone': '022-22067676', 'specialty': 'Pulmonology'},
                {'name': 'PD Hinduja Hospital', 'address': 'Mahim, Mumbai', 'phone': '022-24447000', 'specialty': 'Respiratory'},
            ],
            'Karnataka': [
                {'name': 'Manipal Hospital', 'address': 'HAL Airport Road, Bengaluru', 'phone': '080-25023000', 'specialty': 'Pulmonology'},
                {'name': 'Apollo Hospital', 'address': 'Bannerghatta Road, Bengaluru', 'phone': '080-26304050', 'specialty': 'Respiratory'},
            ],
            'Tamil Nadu': [
                {'name': 'Apollo Hospitals', 'address': 'Greams Road, Chennai', 'phone': '044-28293333', 'specialty': 'Pulmonology'},
                {'name': 'Global Hospital', 'address': 'Perumbakkam, Chennai', 'phone': '044-44777000', 'specialty': 'Respiratory'},
            ],
            'Gujarat': [
                {'name': 'Sterling Hospital', 'address': 'Gurukul Road, Ahmedabad', 'phone': '079-40011000', 'specialty': 'Pulmonology'},
                {'name': 'Apollo Hospital Ahmedabad', 'address': 'Ahmedabad', 'phone': '079-66701800', 'specialty': 'Respiratory'},
            ],
            'Rajasthan': [
                {'name': 'Eternal Hospital', 'address': 'Jagatpura, Jaipur', 'phone': '0141-4747000', 'specialty': 'Respiratory Medicine'},
                {'name': 'Fortis Hospital Jaipur', 'address': 'Jaipur', 'phone': '0141-2547000', 'specialty': 'Pulmonology'},
            ],
            'Kerala': [
                {'name': 'Amrita Institute', 'address': 'Kochi', 'phone': '0484-2801234', 'specialty': 'Pulmonology'},
                {'name': 'Lakeshore Hospital', 'address': 'Kochi', 'phone': '0484-2701032', 'specialty': 'Respiratory'},
            ],
            'Uttar Pradesh': [
                {'name': 'KGMU Respiratory Dept', 'address': 'Lucknow', 'phone': '0522-2257540', 'specialty': 'Pulmonology'},
                {'name': 'Medanta Lucknow', 'address': 'Lucknow', 'phone': '0522-4505050', 'specialty': 'Respiratory'},
            ],
            'West Bengal': [
                {'name': 'Belle Vue Clinic', 'address': 'Loudon Street, Kolkata', 'phone': '033-22877711', 'specialty': 'Pulmonology'},
                {'name': 'Woodlands Hospital', 'address': 'Alipore, Kolkata', 'phone': '033-30903090', 'specialty': 'Respiratory'},
            ],
            'Telangana': [
                {'name': 'Yashoda Hospital', 'address': 'Secunderabad', 'phone': '040-45674567', 'specialty': 'Pulmonology'},
                {'name': 'Apollo Hyderabad', 'address': 'Jubilee Hills, Hyderabad', 'phone': '040-23607777', 'specialty': 'Respiratory'},
            ],
        }
    },

    'CHKPX': {
        'medicines_positive': [
            {'name': 'Acyclovir', 'use': 'Antiviral that reduces severity and duration', 'type': 'Antiviral'},
            {'name': 'Calamine Lotion', 'use': 'Relieves itching and soothes skin rashes', 'type': 'Topical'},
            {'name': 'Paracetamol', 'use': 'Reduces fever and relieves discomfort', 'type': 'Antipyretic'},
            {'name': 'Cetirizine', 'use': 'Antihistamine for itch relief', 'type': 'Antihistamine'},
        ],
        'tips_positive': [
            'Keep nails short and clean to avoid scratching blisters',
            'Bathe with lukewarm water and mild soap',
            'Wear loose cotton clothing to reduce skin irritation',
            'Stay isolated until all blisters have crusted over',
            'Stay well hydrated and eat soft, easy-to-swallow foods',
            'Do NOT use aspirin in children — risk of Reye syndrome',
        ],
        'tips_negative': [
            'Get the varicella (chickenpox) vaccine if not vaccinated',
            'Avoid contact with infected individuals',
            'Maintain good hand hygiene',
            'Keep children vaccinated as per national schedule',
            'Boost immunity with a balanced diet and adequate sleep',
        ],
        'hospitals': {
            'Delhi': [
                {'name': 'Kalawati Saran Hospital', 'address': 'Bangla Sahib Road, Delhi', 'phone': '011-23365525', 'specialty': 'Paediatrics'},
                {'name': 'LNJP Hospital', 'address': 'JLN Marg, Delhi', 'phone': '011-23232400', 'specialty': 'Infectious Disease'},
            ],
            'Maharashtra': [
                {'name': 'BYL Nair Hospital', 'address': 'Mumbai Central', 'phone': '022-23027644', 'specialty': 'Infectious Disease'},
                {'name': 'Lokmanya Tilak Hospital', 'address': 'Sion, Mumbai', 'phone': '022-24076381', 'specialty': 'General Medicine'},
            ],
            'Karnataka': [
                {'name': "Indira Gandhi Children's Hospital", 'address': 'Shivajinagar, Bengaluru', 'phone': '080-22862636', 'specialty': 'Paediatrics'},
                {'name': 'Bowring Hospital', 'address': 'Shivajinagar, Bengaluru', 'phone': '080-25561902', 'specialty': 'General Medicine'},
            ],
            'Tamil Nadu': [
                {'name': 'Institute of Child Health', 'address': 'Egmore, Chennai', 'phone': '044-28194020', 'specialty': 'Paediatrics'},
                {'name': 'Rajiv Gandhi Govt Hospital', 'address': 'Park Town, Chennai', 'phone': '044-25305000', 'specialty': 'Infectious Disease'},
            ],
            'Kerala': [
                {'name': 'SAT Hospital', 'address': 'Thiruvananthapuram', 'phone': '0471-2528386', 'specialty': 'Paediatrics'},
                {'name': 'Government Medical College Thrissur', 'address': 'Thrissur', 'phone': '0487-2200500', 'specialty': 'General Medicine'},
            ],
            'West Bengal': [
                {'name': 'BC Roy Memorial Hospital', 'address': 'Jadavpur, Kolkata', 'phone': '033-24733030', 'specialty': 'Paediatrics'},
                {'name': 'Infectious Disease Hospital', 'address': 'Beliaghata, Kolkata', 'phone': '033-23231473', 'specialty': 'Infectious Disease'},
            ],
            'Gujarat': [
                {'name': 'Civil Hospital Paediatric', 'address': 'Asarwa, Ahmedabad', 'phone': '079-22681234', 'specialty': 'Paediatrics'},
                {'name': "Children's Hospital Vadodara", 'address': 'Vadodara', 'phone': '0265-2411300', 'specialty': 'Paediatrics'},
            ],
            'Uttar Pradesh': [
                {'name': 'KGMU Paediatric Dept', 'address': 'Lucknow', 'phone': '0522-2257540', 'specialty': 'Paediatrics'},
                {'name': 'Sanjay Gandhi PGI', 'address': 'Raebareli Road, Lucknow', 'phone': '0522-2668700', 'specialty': 'Infectious Disease'},
            ],
            'Rajasthan': [
                {'name': 'JK Lon Hospital', 'address': 'Jaipur', 'phone': '0141-2706001', 'specialty': 'Paediatrics'},
                {'name': 'SMS Hospital', 'address': 'Jaipur', 'phone': '0141-2518501', 'specialty': 'General Medicine'},
            ],
            'Telangana': [
                {'name': "Niloufer Children's Hospital", 'address': 'Red Hills, Hyderabad', 'phone': '040-23320131', 'specialty': 'Paediatrics'},
                {'name': 'Osmania General Hospital', 'address': 'Afzalgunj, Hyderabad', 'phone': '040-24600120', 'specialty': 'General Medicine'},
            ],
        }
    },

    'SKIN': {
        'medicines_positive': [
            {'name': 'Hydrocortisone Cream', 'use': 'Reduces inflammation and itching', 'type': 'Topical Steroid'},
            {'name': 'Clotrimazole Cream', 'use': 'Treats fungal skin infections', 'type': 'Antifungal'},
            {'name': 'Mupirocin Ointment', 'use': 'Treats bacterial skin infections', 'type': 'Antibiotic Topical'},
            {'name': 'Cetirizine', 'use': 'Controls allergic skin reactions and itching', 'type': 'Antihistamine'},
        ],
        'tips_positive': [
            'Keep the affected area clean and dry',
            'Avoid scratching to prevent secondary infection',
            'Use fragrance-free soap and moisturizer',
            'Wear breathable, loose cotton clothing',
            'Consult a dermatologist for proper diagnosis',
            'Avoid known allergens and irritants',
        ],
        'tips_negative': [
            'Moisturize daily to maintain skin barrier',
            'Use sunscreen when going outdoors',
            'Stay hydrated for healthy skin',
            'Eat a diet rich in vitamins A, C, and E',
            'Shower after sweating to prevent skin infections',
        ],
        'hospitals': {
            'Delhi': [
                {'name': 'AIIMS Dermatology Dept', 'address': 'Ansari Nagar, New Delhi', 'phone': '011-26588500', 'specialty': 'Dermatology'},
                {'name': 'Safdarjung Hospital Skin Dept', 'address': 'New Delhi', 'phone': '011-26707444', 'specialty': 'Dermatology'},
            ],
            'Maharashtra': [
                {'name': 'KEM Dermatology', 'address': 'Parel, Mumbai', 'phone': '022-24107000', 'specialty': 'Dermatology'},
                {'name': 'Kokilaben Hospital', 'address': 'Andheri West, Mumbai', 'phone': '022-30999999', 'specialty': 'Dermatology'},
            ],
            'Karnataka': [
                {'name': 'NIMHANS Skin Clinic', 'address': 'Hosur Road, Bengaluru', 'phone': '080-46110007', 'specialty': 'Dermatology'},
                {'name': 'Manipal Hospital Dermatology', 'address': 'HAL Road, Bengaluru', 'phone': '080-25023000', 'specialty': 'Skin Specialist'},
            ],
            'Tamil Nadu': [
                {'name': 'Madras Medical College Skin', 'address': 'Park Town, Chennai', 'phone': '044-25305000', 'specialty': 'Dermatology'},
                {'name': 'Apollo Skin Clinic', 'address': 'Greams Road, Chennai', 'phone': '044-28293333', 'specialty': 'Dermatology'},
            ],
            'Kerala': [
                {'name': 'Medical College Dermatology', 'address': 'Thiruvananthapuram', 'phone': '0471-2528386', 'specialty': 'Dermatology'},
                {'name': 'AIMS Kochi Skin Dept', 'address': 'Kochi', 'phone': '0484-2801234', 'specialty': 'Skin Specialist'},
            ],
            'West Bengal': [
                {'name': 'SSKM Dermatology', 'address': 'AJC Bose Road, Kolkata', 'phone': '033-22041739', 'specialty': 'Dermatology'},
                {'name': 'RG Kar Skin Dept', 'address': 'Shyambazar, Kolkata', 'phone': '033-25551876', 'specialty': 'Dermatology'},
            ],
            'Gujarat': [
                {'name': 'Civil Hospital Skin Dept', 'address': 'Asarwa, Ahmedabad', 'phone': '079-22681234', 'specialty': 'Dermatology'},
                {'name': 'Sterling Dermatology', 'address': 'Gurukul Road, Ahmedabad', 'phone': '079-40011000', 'specialty': 'Skin Specialist'},
            ],
            'Rajasthan': [
                {'name': 'SMS Hospital Dermatology', 'address': 'Jaipur', 'phone': '0141-2518501', 'specialty': 'Dermatology'},
                {'name': 'Mahatma Gandhi Hospital', 'address': 'Jaipur', 'phone': '0141-2706700', 'specialty': 'Skin Specialist'},
            ],
            'Uttar Pradesh': [
                {'name': 'KGMU Dermatology Dept', 'address': 'Lucknow', 'phone': '0522-2257540', 'specialty': 'Dermatology'},
                {'name': 'Sanjay Gandhi PGI Skin', 'address': 'Lucknow', 'phone': '0522-2668700', 'specialty': 'Dermatology'},
            ],
            'Telangana': [
                {'name': 'Osmania Hospital Skin Dept', 'address': 'Hyderabad', 'phone': '040-24600120', 'specialty': 'Dermatology'},
                {'name': 'Apollo Skin Hyderabad', 'address': 'Jubilee Hills, Hyderabad', 'phone': '040-23607777', 'specialty': 'Dermatology'},
            ],
        }
    },
}

DEFAULT_HOSPITALS = [
    {'name': 'AIIMS (All India Institute of Medical Sciences)', 'address': 'New Delhi', 'phone': '011-26588500', 'specialty': 'Multi-Specialty'},
    {'name': 'Apollo Hospitals', 'address': 'Multiple locations across India', 'phone': '1860-500-1066', 'specialty': 'Multi-Specialty'},
]