pe_by_diagnosis = {
    "Pneumonia": ["Fever", "Crackles", "Tachypnea", "Dullness to percussion"],
    "Asthma": ["Wheezing", "Accessory muscle use", "Prolonged expiration"],
    "COPD": ["Barrel chest", "Decreased breath sounds", "Prolonged expiration"],
    "Pulmonary embolism": ["Tachypnea", "Clear lungs", "Accentuation of P2", "Calf tenderness"],
    "Pleural effusion": ["Dullness to percussion", "Decreased breath sounds", "Decreased tactile fremitus"],
    "Lung cancer": ["Clubbing", "Localized wheeze", "Decreased breath sounds"],
    "Tuberculosis": ["Fever", "Night sweats", "Weight loss", "Crackles"],
    "Congestive heart failure": ["JVD", "Crackles", "S3 gallop", "Peripheral edema"],
    "Myocardial infarction": ["Levine's sign", "New murmur", "S3 gallop", "Hypotension"],
    "Angina": ["No specific PE", "Possible S4", "Normal heart sounds"],
    "Pericarditis": ["Pericardial friction rub", "Chest pain relieved by sitting forward"],
    "Atrial fibrillation": ["Irregularly irregular pulse", "Absent A wave in JVP"],
    "Hypertension": ["Displaced PMI", "Retinal changes", "S4 heart sound"],
    "Aortic stenosis": ["Crescendo-decrescendo systolic murmur", "Parvus et tardus", "S4"],
    "Mitral regurgitation": ["Holosystolic murmur", "Displaced PMI"],
    "Endocarditis": ["New murmur", "Splinter hemorrhages", "Osler nodes"],
    "Stroke": ["Focal neurological deficit", "Aphasia", "Hemiparesis"],
    "TIA": ["Transient weakness", "Transient aphasia", "Normal PE"],
    "Epilepsy": ["Postictal confusion", "Tongue bite", "Incontinence"],
    "Meningitis": ["Neck stiffness", "Kernig sign", "Brudzinski sign", "Fever"],
    "Parkinson’s disease": ["Resting tremor", "Bradykinesia", "Shuffling gait", "Rigidity"],
    "Migraine": ["Photophobia", "Phonophobia", "Normal PE"],
    "Tension headache": ["Scalp tenderness", "Normal PE"],
    "Multiple sclerosis": ["Optic neuritis", "Spasticity", "Hyperreflexia"],
    "Guillain-Barré syndrome": ["Areflexia", "Flaccid weakness", "Ascending paralysis"],
    "Appendicitis": ["McBurney's point tenderness", "Rebound tenderness", "Rovsing's sign", "Psoas sign"],
    "Cholecystitis": ["Murphy’s sign", "RUQ tenderness", "Guarding"],
    "Pancreatitis": ["Epigastric tenderness", "Cullen’s sign", "Grey-Turner’s sign"],
    "Hepatitis": ["Jaundice", "RUQ tenderness", "Hepatomegaly"],
    "Cirrhosis": ["Ascites", "Spider angiomas", "Caput medusae", "Asterixis"],
    "Peptic ulcer disease": ["Epigastric tenderness", "Normal abdominal sounds"],
    "Gastroenteritis": ["Hyperactive bowel sounds", "Dehydration signs"],
    "Diverticulitis": ["LLQ tenderness", "Fever", "Rebound"],
    "GI bleeding": ["Pallor", "Tachycardia", "Positive occult blood"],
    "Constipation": ["Distended abdomen", "Palpable stool in LLQ"],
    "Diarrhea": ["Dehydration signs", "Hyperactive bowel sounds"],
    "Hemorrhoids": ["Perianal tenderness", "Visible internal or external mass"],
    "Anal fissure": ["Perianal pain", "Tender linear tear"],
    "Colon cancer": ["Pallor", "Palpable abdominal mass", "Occult blood positive"],
    "Ulcerative colitis": ["Tender abdomen", "Rectal bleeding", "No rebound"],
    "Crohn’s disease": ["RLQ tenderness", "Perianal fistula", "Weight loss"],
    "Renal colic": ["CVA tenderness", "Restless appearance"],
    "UTI": ["Suprapubic tenderness", "Fever", "Dysuria"],
    "Pyelonephritis": ["CVA tenderness", "Fever", "Flank pain"],
    "BPH": ["Enlarged, non-tender prostate"],
    "Prostatitis": ["Tender, boggy prostate", "Fever"],
    "Nephrotic syndrome": ["Periorbital edema", "Pitting edema"],
    "CKD": ["Pallor", "Edema", "Pericardial rub (in uremia)"],
    "Kidney cancer": ["Flank mass", "Hematuria"],
    "Bladder cancer": ["Hematuria", "Palpable mass (rare)"],
    "Ovarian cancer": ["Pelvic mass", "Abdominal distension"],
    "Endometrial cancer": ["Abnormal uterine bleeding", "Enlarged uterus"],
    "Cervical cancer": ["Friable cervical lesion", "Irregular bleeding"],
    "Breast cancer": ["Palpable mass", "Skin dimpling", "Axillary lymphadenopathy"],
    "Testicular cancer": ["Painless testicular mass"],
    "Prostate cancer": ["Hard, nodular prostate", "Urinary retention"],
    "Thyroid cancer": ["Firm thyroid nodule", "Cervical lymph nodes"],
    "Lung cancer": ["Clubbing", "Dullness to percussion", "Wheezing"],
    "Liver cancer": ["Hepatomegaly", "Jaundice", "Ascites"],
    "Leukemia": ["Pallor", "Petechiae", "Lymphadenopathy"],
    "Lymphoma": ["Painless lymphadenopathy", "Fever", "Night sweats"],
    "Diabetes mellitus": ["Peripheral neuropathy", "Foot ulcers"],
    "Hyperthyroidism": ["Tachycardia", "Tremor", "Goiter"],
    "Hypothyroidism": ["Bradycardia", "Dry skin", "Slow reflexes"],
    "Obesity": ["Increased BMI", "Abdominal obesity"],
    "Anemia": ["Pallor", "Tachycardia"],
    "Iron deficiency anemia": ["Pallor", "Koilonychia"],
    "Vitamin B12 deficiency": ["Glossitis", "Ataxia", "Decreased vibration sense"],
    "Thalassemia": ["Hepatosplenomegaly", "Pallor"],
    "Sickle cell disease": ["Jaundice", "Splenomegaly", "Leg ulcers"],
    "Rheumatoid arthritis": ["Joint swelling", "Morning stiffness", "Symmetric deformity"],
    "Osteoarthritis": ["Crepitus", "Bony enlargement", "Decreased ROM"],
    "Gout": ["Hot, swollen joint", "Tophus"],
    "Lupus": ["Malar rash", "Joint swelling", "Oral ulcers"],
    "Psoriatic arthritis": ["Skin plaques", "Nail pitting", "Dactylitis"],
    "Fibromyalgia": ["Multiple tender points", "Normal exam otherwise"],
    "Depression": ["Flat affect", "Psychomotor retardation"],
    "Anxiety disorder": ["Restlessness", "Tachycardia"],
    "Schizophrenia": ["Flat affect", "Disorganized speech"],
    "Substance use disorder": ["Track marks", "Pupillary changes"],
    "Delirium": ["Fluctuating consciousness", "Disorientation"],
    "Dementia": ["Impaired memory", "Disorientation"],
    "ADHD": ["Fidgeting", "Short attention span"],
    "Insomnia": ["No abnormal findings"],
    "Sleep apnea": ["Obesity", "Snoring", "Daytime sleepiness"],
    "Skin abscess": ["Localized swelling", "Redness", "Fluctuance"],
    "Cellulitis": ["Warmth", "Erythema", "Tenderness"],
    "Eczema": ["Dry, scaly patches", "Excoriations"],
    "Psoriasis": ["Silvery plaques", "Nail pitting"],
    "Herpes zoster": ["Vesicular rash", "Dermatomal distribution"],
    "Acne": ["Comedones", "Pustules", "Cysts"],
    "Melanoma": ["Irregular pigmented lesion", "Asymmetry"],
    "Basal cell carcinoma": ["Pearly papule", "Telangiectasia"],
    "Squamous cell carcinoma": ["Ulcerated lesion", "Crusting"],
    "Heat stroke": ["Hot, dry skin", "Confusion", "Hypotension"],
    "Hypothermia": ["Cold extremities", "Bradycardia", "Shivering"],
    "Dehydration": ["Dry mucous membranes", "Poor skin turgor"],
    "Electrolyte imbalance": ["Muscle weakness", "Arrhythmia signs"],
    "Sepsis": ["Fever", "Hypotension", "Tachycardia"],
    "Allergic rhinitis": ["Pale boggy turbinates", "Nasal congestion", "Allergic shiners"],
    "Sinusitis": ["Facial tenderness", "Purulent nasal discharge"],
    "Otitis media": ["Bulging tympanic membrane", "Decreased hearing"],
    "Otitis externa": ["Tender tragus", "Ear canal erythema"],
    "Tonsillitis": ["Tonsillar exudates", "Cervical lymphadenopathy", "Fever"],
    "Pharyngitis": ["Pharyngeal erythema", "Enlarged tonsils"],
    "Strep throat": ["Exudative tonsillitis", "Palatal petechiae"],
    "Laryngitis": ["Hoarseness", "Normal PE except for voice"],
    "Epiglottitis": ["Tripod position", "Drooling", "Stridor"],
    "Croup": ["Barking cough", "Inspiratory stridor"],
    "Nasal polyps": ["Nasal obstruction", "Pale polypoid mass"],
    "Conjunctivitis": ["Conjunctival injection", "Discharge"],
    "Blepharitis": ["Red eyelid margin", "Crusting"],
    "Hordeolum (stye)": ["Painful eyelid swelling", "Localized tenderness"],
    "Chalazion": ["Painless eyelid lump", "Non-tender nodule"],
    "Glaucoma": ["Increased intraocular pressure", "Fixed mid-dilated pupil"],
    "Cataract": ["Decreased red reflex", "Cloudy lens"],
    "Retinal detachment": ["Flashes", "Visual field loss"],
    "Macular degeneration": ["Central vision loss", "Drusen on fundus exam"],
    "Diabetic retinopathy": ["Cotton wool spots", "Retinal hemorrhages"],
    "Hypertensive retinopathy": ["AV nicking", "Flame hemorrhages"],
    "Temporal arteritis": ["Scalp tenderness", "Decreased temporal pulse"],
    "Bell's palsy": ["Unilateral facial droop", "Loss of forehead movement"],
    "Trigeminal neuralgia": ["Facial pain", "Normal neuro exam"],
    "Carpal tunnel syndrome": ["Tinel's sign", "Phalen's test"],
    "Cubital tunnel syndrome": ["Ulnar numbness", "Elbow Tinel's"],
    "Radial nerve palsy": ["Wrist drop", "Decreased radial sensation"],
    "Sciatica": ["Positive straight leg raise", "Radicular pain"],
    "Spinal stenosis": ["Neurogenic claudication", "Improves with flexion"],
    "Herniated disc": ["Positive straight leg raise", "Sensory deficit"],
    "Scoliosis": ["Asymmetric shoulder height", "Spinal curvature"],
    "Kyphosis": ["Exaggerated thoracic curve"],
    "Lordosis": ["Exaggerated lumbar curve"],
    "Fracture (any long bone)": ["Swelling", "Tenderness", "Deformity"],
    "Hip fracture": ["Shortened externally rotated leg", "Groin pain"],
    "Osteoporosis": ["Dowager's hump", "Loss of height"],
    "Osteomyelitis": ["Localized warmth", "Tenderness", "Fever"],
    "Septic arthritis": ["Hot, swollen joint", "Decreased ROM", "Fever"],
    "Compartment syndrome": ["Pain out of proportion", "Tense limb", "Paresthesia"],
    "Tendon rupture": ["Loss of active motion", "Gap on palpation"],
    "Sprain": ["Swelling", "Ecchymosis", "Limited ROM"],
    "Meniscus tear": ["Joint line tenderness", "McMurray sign"],
    "ACL injury": ["Positive Lachman", "Knee instability"],
    "Shoulder dislocation": ["Loss of shoulder contour", "Limited ROM"],
    "Rotator cuff tear": ["Painful arc", "Weak external rotation"],
    "Bursitis": ["Localized swelling", "Tenderness"],
    "Tennis elbow": ["Lateral elbow pain", "Pain with resisted extension"],
    "Golfer’s elbow": ["Medial elbow pain", "Pain with resisted flexion"],
    "Trigger finger": ["Clicking during movement", "Finger locking"],
    "Dupuytren's contracture": ["Palmar nodules", "Flexed fingers"],
    "Ganglion cyst": ["Soft mobile wrist lump"],
    "Tenosynovitis": ["Pain with tendon movement", "Swelling"],
    "Plantar fasciitis": ["Heel pain on first step", "Point tenderness"],
    "Achilles tendonitis": ["Posterior ankle pain", "Tenderness at insertion"],
    "Hallux valgus (bunion)": ["Deviated big toe", "MTP joint prominence"],
    "Flat feet": ["Loss of arch", "Overpronation"],
    "Pes cavus": ["High arch", "Claw toes"],
    "Clubfoot": ["Inverted and plantarflexed foot"],
    "Polydactyly": ["Extra digit"],
    "Syndactyly": ["Webbed digits"],
    "Developmental hip dysplasia": ["Asymmetric thigh folds", "Positive Ortolani"],
    "Torticollis": ["Head tilt", "Limited neck rotation"],
    "Hydrocephalus": ["Bulging fontanelle", "Sunsetting eyes"],
    "Spina bifida": ["Midline back dimple", "Hair tuft", "Neurologic deficit"],
    "Cleft palate": ["Palatal gap", "Feeding difficulty"],
    "Laryngomalacia": ["Inspiratory stridor", "Omega-shaped epiglottis"],
    "Bronchiolitis": ["Wheezing", "Tachypnea", "Nasal flaring"],
    "Croup": ["Barking cough", "Stridor"],
    "Measles": ["Koplik spots", "Maculopapular rash"],
    "Rubella": ["Postauricular lymphadenopathy", "Rash"],
    "Mumps": ["Parotid swelling", "Jaw pain"],
    "Varicella": ["Vesicular rash at different stages"],
    "Kawasaki disease": ["Strawberry tongue", "Conjunctivitis", "Extremity desquamation"],
    "Scarlet fever": ["Sandpaper rash", "Pastia lines", "Strawberry tongue"],
    "Hand-foot-mouth disease": ["Oral ulcers", "Vesicles on palms/soles"],
    "Fifth disease": ["Slapped cheek rash", "Lacy extremity rash"],
    "Roseola": ["High fever → rash after defervescence"],
    "Pyloric stenosis": ["Olive-shaped mass", "Projectile vomiting"],
    "Intussusception": ["Sausage-shaped mass", "Currant jelly stool"],
    "Hirschsprung disease": ["Abdominal distension", "Delayed meconium"],
    "Neonatal jaundice": ["Yellow skin/sclera", "Hepatomegaly"],
    "Breastfeeding jaundice": ["Weight loss", "Increased indirect bilirubin"],
    "Failure to thrive": ["Poor weight gain", "Wasted appearance"],
    "Iron deficiency (infant)": ["Pallor", "Irritability"],
    "Lead poisoning": ["Blue gum line", "Developmental delay"],
    "Autism spectrum disorder": ["Poor eye contact", "Repetitive behavior"],
    "Tourette syndrome": ["Motor and vocal tics"],
    "Rickets": ["Bowed legs", "Rachitic rosary"],
    "Scurvy": ["Bleeding gums", "Corkscrew hairs"],
    "Marasmus": ["Wasted appearance", "Loss of fat"],
    "Kwashiorkor": ["Edema", "Skin/hair changes"],
    "Down syndrome": ["Flat facial profile", "Simian crease"],
    "Turner syndrome": ["Short stature", "Webbed neck", "Shield chest"],
    "Klinefelter syndrome": ["Small testes", "Gynecomastia", "Tall stature"],
    "Marfan syndrome": ["Tall stature", "Arm span > height", "Aortic murmur", "Lens dislocation"],
    "Ehlers-Danlos syndrome": ["Joint hypermobility", "Skin hyperextensibility", "Easy bruising"],
    "Neurofibromatosis type 1": ["Café-au-lait spots", "Neurofibromas", "Axillary freckling"],
    "Neurofibromatosis type 2": ["Bilateral hearing loss", "Vestibular schwannomas"],
    "Tuberous sclerosis": ["Ash-leaf spots", "Facial angiofibromas", "Shagreen patch"],
    "Von Hippel-Lindau disease": ["Hemangioblastomas", "Retinal angiomas"],
    "Huntington disease": ["Chorea", "Dementia", "Mood change"],
    "Wilson disease": ["Kayser-Fleischer rings", "Tremor", "Hepatomegaly"],
    "Hemochromatosis": ["Bronze skin", "Hepatomegaly", "Joint pain"],
    "Phenylketonuria (PKU)": ["Musty odor", "Intellectual disability", "Fair complexion"],
    "Galactosemia": ["Jaundice", "Hepatomegaly", "Cataracts"],
    "Maple syrup urine disease": ["Maple syrup odor", "Lethargy", "Seizures"],
    "Ornithine transcarbamylase deficiency": ["Hyperammonemia", "Vomiting", "Confusion"],
    "Lesch-Nyhan syndrome": ["Self-mutilation", "Gout", "Dystonia"],
    "G6PD deficiency": ["Jaundice", "Dark urine", "Fatigue after infection or fava beans"],
    "Alpha-1 antitrypsin deficiency": ["Early emphysema", "Liver disease", "Barrel chest"],
    "Cystic fibrosis": ["Nasal polyps", "Crackles", "Failure to thrive"],
    "Hereditary spherocytosis": ["Splenomegaly", "Jaundice", "Anemia"],
    "Sickle cell anemia": ["Dactylitis", "Leg ulcers", "Splenomegaly"],
    "Thalassemia major": ["Hepatosplenomegaly", "Pallor", "Skeletal deformities"],
    "Hemophilia A": ["Joint swelling", "Prolonged bleeding", "Bruising"],
    "Von Willebrand disease": ["Nosebleeds", "Easy bruising", "Menorrhagia"],
    "ITP (Immune thrombocytopenic purpura)": ["Petechiae", "Purpura", "Bleeding gums"],
    "TTP (Thrombotic thrombocytopenic purpura)": ["Fever", "Petechiae", "Neurologic findings"],
    "DIC (Disseminated intravascular coagulation)": ["Bleeding", "Petechiae", "Hypotension"],
    "AML (Acute myeloid leukemia)": ["Gingival hypertrophy", "Pallor", "Bruising"],
    "ALL (Acute lymphoblastic leukemia)": ["Lymphadenopathy", "Pallor", "Fever"],
    "CML (Chronic myeloid leukemia)": ["Splenomegaly", "Fatigue"],
    "CLL (Chronic lymphocytic leukemia)": ["Lymphadenopathy", "Hepatosplenomegaly"],
    "Polycythemia vera": ["Ruddy face", "Splenomegaly", "Headache"],
    "Myelofibrosis": ["Massive splenomegaly", "Fatigue", "Weight loss"],
    "Multiple myeloma": ["Bone pain", "Pallor", "Fractures"],
    "MGUS": ["No specific PE", "Normal findings"],
    "Waldenström’s macroglobulinemia": ["Vision changes", "Hepatosplenomegaly"],
    "Hodgkin lymphoma": ["Painless lymphadenopathy", "Night sweats", "Pruritus"],
    "Non-Hodgkin lymphoma": ["Lymph node mass", "Fatigue", "Weight loss"],
    "Pancreatic cancer": ["Courvoisier’s sign", "Weight loss", "Jaundice"],
    "Gallbladder cancer": ["RUQ mass", "Jaundice"],
    "Cholangiocarcinoma": ["Painless jaundice", "Hepatomegaly"],
    "Esophageal cancer": ["Dysphagia", "Weight loss"],
    "Gastric cancer": ["Epigastric mass", "Cachexia"],
    "Colon cancer": ["Palpable mass", "Occult blood", "Pallor"],
    "Rectal cancer": ["Rectal mass", "Occult blood"],
    "Renal cell carcinoma": ["Flank mass", "Hematuria"],
    "Bladder cancer": ["Gross hematuria", "Pelvic mass"],
    "Prostate cancer": ["Hard nodular prostate", "Urinary retention"],
    "Testicular torsion": ["High-riding testis", "Absent cremasteric reflex"],
    "Epididymitis": ["Scrotal tenderness", "Swelling", "Prehn sign"],
    "Varicocele": ["Bag of worms feeling", "Left-sided mass"],
    "Hydrocele": ["Transilluminates", "Soft scrotal swelling"],
    "Phimosis": ["Unable to retract foreskin"],
    "Paraphimosis": ["Trapped foreskin behind glans"],
    "Balanitis": ["Redness", "Painful glans"],
    "Penile cancer": ["Ulcerated penile lesion"],
    "Cervical polyp": ["Friable mass", "Spotting"],
    "Ovarian torsion": ["Adnexal tenderness", "Abdominal guarding"],
    "Endometriosis": ["Tender nodules", "Retroverted uterus"],
    "Uterine fibroids": ["Enlarged irregular uterus"],
    "Pelvic inflammatory disease": ["Cervical motion tenderness", "Adnexal tenderness"],
    "Ectopic pregnancy": ["Adnexal mass", "Tenderness", "Unstable vitals"],
    "Miscarriage": ["Cervical dilation", "Bleeding"],
    "Pre-eclampsia": ["Hypertension", "Edema", "Hyperreflexia"],
    "HELLP syndrome": ["RUQ pain", "Edema", "Jaundice"],
    "Placenta previa": ["Painless vaginal bleeding"],
    "Placental abruption": ["Painful bleeding", "Rigid uterus"],
    "Preterm labor": ["Regular contractions", "Cervical dilation < 37 weeks"],
    "PROM": ["Pooling of fluid", "Positive nitrazine"],
    "Chorioamnionitis": ["Fever", "Uterine tenderness"],
    "Postpartum hemorrhage": ["Heavy bleeding", "Soft uterus"],
    "Mastitis": ["Breast tenderness", "Redness", "Fever"],
    "Breast abscess": ["Fluctuant tender mass", "Fever"],
    "Polycystic ovarian syndrome": ["Hirsutism", "Acne", "Obesity"],
    "Menopause": ["Hot flashes", "Vaginal dryness"],
    "Hypogonadism": ["Small testes", "Decreased body hair"],
    "Gynecomastia": ["Breast enlargement", "Tenderness"],
    "Infertility (female)": ["Normal PE or signs of hormonal imbalance"],
    "Infertility (male)": ["Testicular atrophy", "Varicocele"],
    "Erectile dysfunction": ["Normal exam or penile abnormalities"],
    "Priapism": ["Painful erection", "Engorged penis"],
    "Urinary incontinence": ["Normal PE", "Perineal skin irritation"],
    "Overactive bladder": ["Urge symptoms", "Normal PE"],
    "Interstitial cystitis": ["Bladder tenderness", "No infection signs"],
    "Neurogenic bladder": ["Post-void residual", "Neurologic signs"],
    "Urethral stricture": ["Weak stream", "Post-void dribbling"],
    "Kidney transplant": ["Surgical scar", "Normal or tender graft site"],
    "Liver transplant": ["Abdominal scar", "Jaundice", "Hepatomegaly"],
    "Heart transplant": ["Surgical scar", "Bradycardia", "Muffled heart sounds"],
    "Lung transplant": ["Diminished breath sounds", "Incision site"],
    "Dialysis patient": ["AV fistula", "Edema", "Uremic frost"],
    "Hemodialysis complications": ["AV fistula thrill", "Hypotension", "Edema"],
    "Peritoneal dialysis complications": ["Peritonitis signs", "Abdominal tenderness"],
    "Organ rejection (general)": ["Fever", "Tender transplant site"],
    "Post-transplant infection": ["Fever", "Lymphadenopathy", "Incision inflammation"],
    "Immunodeficiency (general)": ["Oral thrush", "Skin infections"],
    "HIV acute infection": ["Fever", "Rash", "Oral ulcers"],
    "HIV chronic infection": ["Oral thrush", "Lymphadenopathy", "Wasting"],
    "AIDS defining illness": ["Cachexia", "Opportunistic infections signs"],
    "Pneumocystis pneumonia": ["Dry cough", "Hypoxia", "Crackles"],
    "Kaposi sarcoma": ["Purple skin lesions", "Oral lesions"],
    "Toxoplasmosis": ["Focal neuro signs", "Confusion"],
    "CMV infection": ["Retinitis signs", "Abdominal pain", "Diarrhea"],
    "Oral candidiasis": ["White plaques on tongue", "Erythematous base"],
    "Esophageal candidiasis": ["Odynophagia", "Oral thrush"],
    "Cryptococcal meningitis": ["Headache", "Stiff neck", "Altered sensorium"],
    "Histoplasmosis": ["Hepatosplenomegaly", "Fever", "Pulmonary findings"],
    "Aspergillosis": ["Hemoptysis", "Fever", "Crackles"],
    "COVID long-term effects": ["Fatigue", "Tachycardia", "Brain fog"],
    "Long QT syndrome": ["Syncope", "Bradycardia", "No PE or murmur"],
    "Brugada syndrome": ["Syncope", "Normal PE", "Family history"],
    "Atrial septal defect": ["Fixed split S2", "Systolic ejection murmur"],
    "Ventricular septal defect": ["Holosystolic murmur", "Thrill at LLSB"],
    "Patent ductus arteriosus": ["Continuous machinery murmur", "Bounding pulse"],
    "Coarctation of aorta": ["Radio-femoral delay", "High BP upper limbs"],
    "Tetralogy of Fallot": ["Cyanosis", "Systolic murmur", "Clubbing"],
    "Transposition of great arteries": ["Cyanosis", "Tachypnea"],
    "Tricuspid atresia": ["Cyanosis", "Murmur"],
    "Ebstein anomaly": ["Triphasic murmur", "Cyanosis"],
    "Pulmonary stenosis": ["Systolic murmur", "Cyanosis"],
    "Total anomalous pulmonary venous return": ["Cyanosis", "Heart failure signs"],
    "Hypoplastic left heart syndrome": ["Cyanosis", "Poor perfusion"],
    "Turner syndrome cardiac": ["Webbed neck", "Coarctation murmur"],
    "Down syndrome cardiac": ["AV canal defect murmur", "Hypotonia"],
    "DiGeorge syndrome": ["Cleft palate", "Hypocalcemia signs", "Conotruncal murmur"],
    "Williams syndrome": ["Elfin face", "Supravalvular aortic stenosis murmur"],
    "Noonan syndrome": ["Low ears", "Pulmonary stenosis murmur"],
    "Metabolic syndrome": ["Central obesity", "HTN", "Acanthosis nigricans"],
    "Obstructive sleep apnea": ["Obesity", "Neck circumference ↑", "Snoring"],
    "Narcolepsy": ["Cataplexy", "Sleep attacks"],
    "Restless legs syndrome": ["Urge to move legs", "Sleep disturbance"],
    "Insomnia disorder": ["No abnormal PE"],
    "Generalized anxiety disorder": ["Restlessness", "Muscle tension"],
    "Panic disorder": ["Hyperventilation", "Tachycardia", "Sweating"],
    "PTSD": ["Startle response", "Avoidance behavior"],
    "OCD": ["Repetitive behavior", "Anxiety"],
    "Bipolar disorder": ["Mood swings", "Pressured speech"],
    "Schizoaffective disorder": ["Mood symptoms", "Psychosis signs"],
    "Major depressive disorder": ["Flat affect", "Slow speech"],
    "Dysthymia": ["Low mood", "Poor eye contact"],
    "Adjustment disorder": ["Tearfulness", "Mild anxiety"],
    "Grief reaction": ["Crying", "Normal vital signs"],
    "Substance intoxication": ["Altered mental status", "Pupillary changes"],
    "Substance withdrawal": ["Tremor", "Sweating", "Tachycardia"],
    "Alcohol use disorder": ["Hepatomegaly", "Tremor", "Spider angiomas"],
    "Wernicke encephalopathy": ["Confusion", "Ataxia", "Nystagmus"],
    "Korsakoff syndrome": ["Amnesia", "Confabulation"],
    "Opioid overdose": ["Pinpoint pupils", "Respiratory depression"],
    "Benzodiazepine overdose": ["Drowsiness", "Ataxia"],
    "Stimulant overdose": ["Tachycardia", "Agitation", "Mydriasis"],
    "Delirium tremens": ["Tachycardia", "Agitation", "Hallucinations"],
    "Barbiturate overdose": ["Coma", "Hypotension", "Bradycardia"],
    "Lead poisoning (adult)": ["Foot drop", "Abdominal pain", "Anemia"],
    "Carbon monoxide poisoning": ["Cherry red lips", "Headache", "Confusion"],
    "Cyanide poisoning": ["Smell of bitter almonds", "Seizures", "Lactic acidosis"],
    "Organophosphate poisoning": ["Salivation", "Lacrimation", "Bradycardia"],
    "Arsenic poisoning": ["Aldrich-Mees lines", "Diarrhea", "Garlic breath"],
    "Methanol poisoning": ["Visual disturbance", "Anion gap acidosis"],
    "Ethylene glycol poisoning": ["Hypocalcemia", "Flank pain", "CNS depression"],
    "Salicylate toxicity": ["Tinnitus", "Respiratory alkalosis", "Vomiting"],
    "Iron overdose": ["GI bleeding", "Hypotension", "Lethargy"],
    "Acetaminophen overdose": ["RUQ pain", "Jaundice", "Elevated LFTs"],
    "NSAID adverse effect": ["Epigastric pain", "GI bleeding"],
    "Anaphylaxis": ["Hypotension", "Urticaria", "Wheezing"],
    "Urticaria": ["Raised itchy wheals", "Angioedema"],
    "Angioedema": ["Lip/tongue swelling", "Airway compromise signs"],
    "Contact dermatitis": ["Erythematous rash", "Vesicles"],
    "Drug rash": ["Maculopapular rash", "Fever", "Itching"],
    "Erythema multiforme": ["Target lesions", "Mucosal involvement"],
    "Steven Johnson syndrome": ["Widespread rash", "Mucosal sloughing"],
    "Toxic epidermal necrolysis": ["Skin detachment", "Nikolsky sign"],
    "Herpes simplex virus": ["Grouped vesicles", "Painful ulcer"],
    "Human papillomavirus (genital warts)": ["Cauliflower lesions", "Perianal distribution"],
    "Syphilis (primary)": ["Painless ulcer (chancre)", "Inguinal lymphadenopathy"],
    "Syphilis (secondary)": ["Rash on palms/soles", "Condyloma lata"],
    "Gonorrhea": ["Purulent discharge", "Dysuria"],
    "Chlamydia": ["Mucopurulent discharge", "Friable cervix"],
    "Trichomoniasis": ["Frothy green discharge", "Strawberry cervix"],
    "Bacterial vaginosis": ["Thin grey discharge", "Fishy odor"],
    "Candidal vaginitis": ["White clumpy discharge", "Itchy vulva"],
    "Pelvic inflammatory disease": ["Cervical motion tenderness", "Fever", "Adnexal tenderness"],
    "Genital herpes": ["Painful genital ulcers", "Tender lymphadenopathy"],
    "Chancroid": ["Painful genital ulcer", "Fluctuant bubo"],
    "Lymphogranuloma venereum": ["Small painless ulcer", "Tender inguinal lymphadenopathy"],
    "Granuloma inguinale": ["Painless beefy red ulcer"],
    "Zika virus": ["Maculopapular rash", "Conjunctivitis", "Arthralgia"],
    "Dengue fever": ["Retro-orbital pain", "Rash", "Petechiae"],
    "Chikungunya": ["Arthritis", "Rash", "Fever"],
    "Yellow fever": ["Jaundice", "Fever", "Hematemesis"],
    "Malaria": ["Cyclic fever", "Hepatosplenomegaly"],
    "Babesiosis": ["Hemolytic anemia", "Fever", "Jaundice"],
    "Leishmaniasis": ["Skin ulcers", "Hepatosplenomegaly"],
    "Echinococcus infection": ["Hepatic cysts", "RUQ mass"],
    "Schistosomiasis": ["Hematuria", "Hepatosplenomegaly"],
    "Toxocariasis": ["Hepatomegaly", "Eosinophilia"],
    "Strongyloidiasis": ["Abdominal pain", "Rash", "Wheezing"],
    "Ascariasis": ["Cough", "Abdominal discomfort"],
    "Hookworm infection": ["Pallor", "Abdominal pain"],
    "Enterobiasis (pinworm)": ["Perianal itching"],
    "Trichinosis": ["Periorbital edema", "Myalgia", "Eosinophilia"],
    "Giardiasis": ["Greasy stools", "Bloating", "Weight loss"],
    "Amebiasis": ["Dysentery", "Hepatic tenderness"],
    "Cryptosporidiosis": ["Watery diarrhea", "Dehydration"],
    "Norovirus": ["Vomiting", "Diarrhea"],
    "Rotavirus": ["Diarrhea", "Dehydration"],
    "Clostridioides difficile": ["Watery diarrhea", "Abdominal pain"],
    "Traveler’s diarrhea (E. coli)": ["Abdominal cramping", "Watery diarrhea"],
    "Salmonella enteritis": ["Fever", "Diarrhea", "Abdominal tenderness"],
    "Typhoid fever": ["Rose spots", "Relative bradycardia"],
    "Shigellosis": ["Bloody diarrhea", "Abdominal cramping"],
    "Campylobacter infection": ["Fever", "Bloody stools"],
    "Listeriosis": ["Fever", "Neck stiffness (in neonates)"],
    "Brucellosis": ["Undulating fever", "Arthralgia", "Hepatosplenomegaly"],
    "Q fever": ["Pneumonia signs", "Fever", "Hepatitis signs"],
    "Leptospirosis": ["Conjunctival suffusion", "Jaundice", "Myalgia"],
    "Rickettsial infection": ["Fever", "Rash", "Eschar"],
    "Ebola virus": ["Hemorrhagic signs", "Hypotension"],
    "Marburg virus": ["Bleeding", "High fever"],
    "Rabies": ["Hydrophobia", "Aerophobia", "Agitation"],
    "Tetanus": ["Trismus", "Muscle rigidity", "Opisthotonos"],
    "Botulism": ["Descending paralysis", "Diplopia", "Hypotonia"],
    "Anthrax (cutaneous)": ["Painless black ulcer", "Surrounding edema"],
    "Plague": ["Buboes", "Fever", "Hemoptysis (if pneumonic)"],
    "Tularemia": ["Ulceroglandular lesion", "Lymphadenopathy"],
    "Smallpox": ["Vesicular rash all same stage", "Fever"],
    "Monkeypox": ["Vesiculopustular rash", "Lymphadenopathy"],
    "Sarcoidosis": ["Bilateral hilar lymphadenopathy", "Skin nodules"],
    "Amyloidosis": ["Macroglossia", "Periorbital purpura"],
    "Systemic sclerosis": ["Skin tightening", "Sclerodactyly", "Raynaud's"],
    "Sjogren’s syndrome": ["Dry eyes", "Parotid swelling", "Dry mouth"],
    "Mixed connective tissue disease": ["Raynaud's", "Swollen hands"],
    "Antiphospholipid syndrome": ["Livedo reticularis", "DVT history"],
    "Behçet’s disease": ["Oral ulcers", "Genital ulcers", "Uveitis"],
    "Takayasu arteritis": ["Asymmetric BP", "Bruits", "Claudication"],
    "Temporal arteritis": ["Tender temporal artery", "Jaw claudication"],
    "Polyarteritis nodosa": ["Livedo reticularis", "Abdominal pain", "HTN"],
    "Granulomatosis with polyangiitis": ["Nasal crusting", "Hematuria", "Hemoptysis"],
    "Eosinophilic granulomatosis with polyangiitis": ["Asthma", "Neuropathy"],
    "Microscopic polyangiitis": ["Hematuria", "Purpura", "Fever"],
    "Goodpasture syndrome": ["Hemoptysis", "Hematuria"],
    "Alport syndrome": ["Hearing loss", "Hematuria"],
    "Fabry disease": ["Angiokeratomas", "Neuropathy", "Proteinuria"],
    "Hunter syndrome": ["Coarse facial features", "Hepatosplenomegaly"],
    "Hurler syndrome": ["Developmental delay", "Corneal clouding"],
    "Gaucher disease": ["Hepatosplenomegaly", "Bone crisis"],
    "Niemann-Pick disease": ["Cherry-red spot", "Hepatosplenomegaly"],
    "Tay-Sachs disease": ["Cherry-red spot", "Hyperreflexia"],
    "Krabbe disease": ["Optic atrophy", "Developmental regression"],
    "Metachromatic leukodystrophy": ["Ataxia", "Dementia"],
    "X-linked agammaglobulinemia": ["Recurrent infections", "No tonsils"],
    "Selective IgA deficiency": ["Anaphylaxis to blood", "Recurrent GI infections"],
    "Common variable immunodeficiency": ["Recurrent infections", "Autoimmune disease"],
    "Hyper IgE syndrome": ["Coarse facies", "Eczema", "Recurrent abscesses"],
    "Wiskott-Aldrich syndrome": ["Eczema", "Thrombocytopenia", "Infections"],
    "SCID (Severe combined immunodeficiency)": ["Chronic diarrhea", "Failure to thrive"],
    "Ataxia telangiectasia": ["Ataxia", "Telangiectasias", "Frequent infections"],
    "Bloom syndrome": ["Photosensitivity", "Growth delay"],
    "Fanconi anemia": ["Short stature", "Pancytopenia", "Abnormal thumbs"],
    "Diamond-Blackfan anemia": ["Pallor", "Short stature", "Triphalangeal thumb"],
    "Neutropenia": ["Recurrent infections", "Mucosal ulcers"],
    "Thrombocytopenia": ["Petechiae", "Easy bruising"],
    "Neonatal sepsis": ["Temperature instability", "Poor feeding"],
    "Neonatal jaundice (pathologic)": ["Jaundice <24h", "Elevated direct bilirubin"],
    "Neonatal hypoglycemia": ["Jitteriness", "Apnea"],
    "Neonatal abstinence syndrome": ["Irritability", "Sneezing", "Diarrhea"],
    "Meconium aspiration": ["Grunting", "Cyanosis"],
    "Respiratory distress syndrome (preemie)": ["Tachypnea", "Nasal flaring", "Grunting"],
    "Transient tachypnea of newborn": ["Tachypnea", "Clear lungs"],
    "Birth trauma (clavicle fx)": ["Crepitus", "Asymmetric movement"],
    "Erb-Duchenne palsy": ["Arm adducted", "Internally rotated"],
    "Klumpke palsy": ["Claw hand", "Horner syndrome"],
    "Necrotizing enterocolitis": ["Abdominal distension", "Bloody stools"],
    "Omphalitis": ["Red, swollen umbilicus"],
    "Umbilical granuloma": ["Moist red mass at umbilicus"],
    "Gastroschisis": ["Bowel outside abdomen", "No covering sac"],
    "Omphalocele": ["Midline defect", "Sac-covered viscera"],
    "Bladder exstrophy": ["Visible bladder mucosa"],
    "Hypospadias": ["Abnormal urethral meatus"],
    "Epispadias": ["Dorsal urethral opening"],
    "Cryptorchidism": ["Empty scrotum", "Palpable testis in inguinal canal"]
}
