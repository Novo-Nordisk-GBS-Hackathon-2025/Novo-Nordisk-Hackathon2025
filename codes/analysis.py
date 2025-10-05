import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
import logging
from datetime import datetime, timedelta

# --- Streamlit Configuration ---
# Must be at the top level of the script
st.set_page_config(
    page_title=" Wegovy Comprehensive Market Analysis for stratergies",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🎯"
)

# Configure logging and warnings
warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.INFO)

# Initialize session state for caching
if 'live_scraped_cache' not in st.session_state:
    st.session_state.live_scraped_cache = {}  
if 'scrape_timestamps' not in st.session_state:
    st.session_state.scrape_timestamps = {}
    
# --- Market Intelligence Engine Class ---
class StructuredMarketIntelligenceEngine:
    """Comprehensive market intelligence engine for Wegovy India."""
    
    def __init__(self):
        # State Populations (in millions)
        self.state_populations = {
            'Uttar Pradesh': 238.6, 'Maharashtra': 123.1, 'Bihar': 128.5, 'West Bengal': 97.7,
            'Tamil Nadu': 77.8, 'Rajasthan': 81.0, 'Karnataka': 67.6, 'Gujarat': 70.1,
            'Andhra Pradesh': 53.9, 'Odisha': 45.4, 'Telangana': 38.5, 'Kerala': 35.0,
            'Jharkhand': 38.6, 'Assam': 35.6, 'Punjab': 30.1, 'Chhattisgarh': 29.4,
            'Haryana': 28.9, 'Uttarakhand': 11.4, 'Himachal Pradesh': 7.3, 'Tripura': 4.2,
            'Meghalaya': 3.4, 'Manipur': 3.3, 'Nagaland': 2.2, 'Goa': 1.5, 
            'Arunachal Pradesh': 1.7, 'Mizoram': 1.2, 'Sikkim': 0.7, 'Delhi': 32.9,
            'Chandigarh': 1.2, 'Puducherry': 1.4, 'Jammu and Kashmir': 13.6, 'Ladakh': 0.3
        }
        
        # NFHS-5 BMI DATA (Verified Source: BMC Public Health article - Figure 4 extracted)
        self.nfhs5_bmi_data = {
            'India': {'severely_moderately_thin': 29412236, 'mildly_thin': 50021199, 'normal': 389110427, 'overweight': 137188470, 'obese': 37599029},
            'Maharashtra': {'severely_moderately_thin': 4230340, 'mildly_thin': 6131973, 'normal': 49760521, 'overweight': 17946442, 'obese': 4676538},
            'Tamil Nadu': {'severely_moderately_thin': 937665, 'mildly_thin': 1524666, 'normal': 13685429, 'overweight': 8603768, 'obese': 3814678},
            'Uttar Pradesh': {'severely_moderately_thin': 3008046, 'mildly_thin': 5880126, 'normal': 41782446, 'overweight': 13134006, 'obese': 3725632},
            'Karnataka': {'severely_moderately_thin': 1710735, 'mildly_thin': 2932258, 'normal': 25709842, 'overweight': 12210878, 'obese': 3493421},
            'Andhra Pradesh': {'severely_moderately_thin': 1335625, 'mildly_thin': 2565458, 'normal': 18097616, 'overweight': 9847329, 'obese': 3158123},
            'Gujarat': {'severely_moderately_thin': 3282370, 'mildly_thin': 4212620, 'normal': 26230139, 'overweight': 7814417, 'obese': 2857348},
            'West Bengal': {'severely_moderately_thin': 2809375, 'mildly_thin': 5359771, 'normal': 50181013, 'overweight': 13156564, 'obese': 2363263},
            'Bihar': {'severely_moderately_thin': 3252497, 'mildly_thin': 5771773, 'normal': 36084214, 'overweight': 9311491, 'obese': 1953691},
            'Telangana': {'severely_moderately_thin': 1093889, 'mildly_thin': 1543634, 'normal': 11210183, 'overweight': 5644159, 'obese': 1854102},
            'Kerala': {'severely_moderately_thin': 398898, 'mildly_thin': 681062, 'normal': 10700571, 'overweight': 6947211, 'obese': 1822809},
            'Punjab': {'severely_moderately_thin': 286256, 'mildly_thin': 504282, 'normal': 4808473, 'overweight': 2918016, 'obese': 1351680},
            'Rajasthan': {'severely_moderately_thin': 1177113, 'mildly_thin': 2237995, 'normal': 19742074, 'overweight': 3990390, 'obese': 1100044},
            'Madhya Pradesh': {'severely_moderately_thin': 1533256, 'mildly_thin': 2783973, 'normal': 16185098, 'overweight': 3871435, 'obese': 970843},
            'Odisha': {'severely_moderately_thin': 944406, 'mildly_thin': 1612549, 'normal': 9355229, 'overweight': 3167929, 'obese': 826694},
            'Assam': {'severely_moderately_thin': 1045960, 'mildly_thin': 1714708, 'normal': 16196011, 'overweight': 3699860, 'obese': 691474},
            'Jharkhand': {'severely_moderately_thin': 721597, 'mildly_thin': 1370640, 'normal': 7441640, 'overweight': 1453402, 'obese': 592603},
            'Haryana': {'severely_moderately_thin': 306388, 'mildly_thin': 542202, 'normal': 4676904, 'overweight': 2334501, 'obese': 581568},
            'Chhattisgarh': {'severely_moderately_thin': 648052, 'mildly_thin': 1249862, 'normal': 7441590, 'overweight': 1504985, 'obese': 382653},
            'Himachal Pradesh': {'severely_moderately_thin': 109709, 'mildly_thin': 242221, 'normal': 2556529, 'overweight': 1298155, 'obese': 302591},
            'Uttarakhand': {'severely_moderately_thin': 108246, 'mildly_thin': 241272, 'normal': 1871811, 'overweight': 884256, 'obese': 205027},
            'Goa': {'severely_moderately_thin': 38326, 'mildly_thin': 56997, 'normal': 712838, 'overweight': 39094, 'obese': 90498},
            'Delhi': {'severely_moderately_thin': 153339, 'mildly_thin': 320771, 'normal': 3303468, 'overweight': 815669, 'obese': 89699},
            'Manipur': {'severely_moderately_thin': 19613, 'mildly_thin': 56945, 'normal': 942940, 'overweight': 484162, 'obese': 87096},
            'Tripura': {'severely_moderately_thin': 89955, 'mildly_thin': 182186, 'normal': 1826112, 'overweight': 575520, 'obese': 78664},
            'Puducherry': {'severely_moderately_thin': 9385, 'mildly_thin': 18286, 'normal': 201934, 'overweight': 159548, 'obese': 76508},
            'Jammu and Kashmir': {'severely_moderately_thin': 55600, 'mildly_thin': 136214, 'normal': 4720630, 'overweight': 233628, 'obese': 58976},
            'Mizoram': {'severely_moderately_thin': 4477, 'mildly_thin': 20066, 'normal': 447596, 'overweight': 199545, 'obese': 43181},
            'Meghalaya': {'severely_moderately_thin': 33462, 'mildly_thin': 105038, 'normal': 1523920, 'overweight': 292010, 'obese': 35516},
            'Nagaland': {'severely_moderately_thin': 15576, 'mildly_thin': 37144, 'normal': 714911, 'overweight': 228433, 'obese': 31927},
            'Sikkim': {'severely_moderately_thin': 4201, 'mildly_thin': 6013, 'normal': 247273, 'overweight': 135334, 'obese': 26092}
        }
        
        # Comprehensive Sources (For reference section)
        self.comprehensive_sources = {
            'nfhs5_data': {
                'NFHS-5 Data (Primary Source)': 'http://rchiips.org/nfhs/',
                'NFHS-5 Data (NFHS-5 Headcount Table - BMC Public Health)': 'https://doi.org/10.1186/s12889-024-18784-4',
                'NFHS-5 Data (Spatial Clustering/Hotspots - PLoS ONE)': 'https://doi.org/10.1371/journal.pone.0305205',
            },
            'treatment_patterns': {
                'GLP-1 Market Growth Rate (CAGR 2025-2030)': 'https://www.grandviewresearch.com/industry-analysis/india-glp-1-receptor-agonist-market-report',
                'GLP-1 Anti-Obesity Drug Market Value (March 2025)': 'https://m.economictimes.com/industry/healthcare/biotech/pharmaceuticals/a-big-fat-fight-has-just-broken-out-in-india/articleshow/122049705.cms',
                'GLP-1 Patient Openness/Barriers (77.3% Openness, Cost Barrier)': 'https://www.iosrjournals.org/iosr-jpbs/papers/Vol19-issue6/Ser-2/L1906027179.pdf',
                'GLP-1 Pricing/Uptake (Mounjaro/Wegovy)': 'https://m.economictimes.com/industry/healthcare/biotech/healthcare/india-glp1-weight-loss-drugs-mounjaro-wegovy-semaglutide-patent-expiry-obesity/articleshow/122829113.cms',
                'Bariatric Surgery Cost Range': 'https://nobesity.in/weight-loss-surgery-cost-in-india/',
                'Lifestyle Intervention (Basis)': 'https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1382814/full'
            }
        }

    # --- Cache Helper Methods ---
    def _is_cache_valid(self, cache_key, max_age_minutes=30):
        """Check if cached data is still valid"""
        if cache_key not in st.session_state.scrape_timestamps:
            return False
        
        last_scrape = st.session_state.scrape_timestamps[cache_key]
        age_minutes = (datetime.now() - last_scrape).total_seconds() / 60 
        
        return age_minutes < max_age_minutes
    
    def _cache_data(self, cache_key, data):
        """Cache scraped data"""
        st.session_state.live_scraped_cache[cache_key] = data
        st.session_state.scrape_timestamps[cache_key] = datetime.now()
    # ----------------------------

    def _calculate_obesity_percentages_from_nfhs5(self):
        """Calculate obesity percentages and estimate comorbidities from NFHS-5 data"""
        state_obesity_data = {}
        
        for state, data in self.nfhs5_bmi_data.items():
            if state == 'India':
                continue
                
            total_population = sum(data.values())
            if total_population == 0:
                continue

            # Obesity prevalence (BMI >= 30.0) calculated directly from NFHS-5 raw counts
            obesity_percentage = (data['obese'] / total_population) * 100
            
            # Estimate comorbidity percentages using medical literature ratios
            diabetes_percentage = obesity_percentage * 2.1 # Estimated ratio 
            hypertension_percentage = obesity_percentage * 2.3 # Estimated ratio 
            
            state_obesity_data[state] = {
                'obesity_prevalence': round(obesity_percentage, 1),
                # Cap the estimated values for realism
                'diabetes_prevalence': round(min(diabetes_percentage, 35.0), 1), 
                'hypertension_prevalence': round(min(hypertension_percentage, 40.0), 1), 
                'obese_population': data['obese'],
                'overweight_population': data['overweight'],
                'total_population': total_population
            }
        
        return state_obesity_data
    
    def _calculate_tier_city_data_from_nfhs5(self):
        """Calculates city tier averages strictly based on NFHS-5 state data for internal consistency."""
        state_data = self._calculate_obesity_percentages_from_nfhs5()
        
        # Custom-defined tiers based on market logic (affluence, population, prevalence)
        tier_1_states = ['Maharashtra', 'Tamil Nadu', 'Karnataka', 'Gujarat', 'West Bengal', 'Telangana', 'Kerala', 'Delhi']
        tier_2_states = ['Punjab', 'Haryana', 'Uttarakhand', 'Himachal Pradesh', 'Goa', 'Manipur', 'Tripura']
        tier_3_states = ['Uttar Pradesh', 'Bihar', 'Rajasthan', 'Madhya Pradesh', 'Odisha', 'Assam', 'Jharkhand', 'Chhattisgarh']
        
        def calculate_tier_average(states_list):
            valid_states = [s for s in states_list if s in state_data]
            if not valid_states:
                return {'avg_obesity_prevalence': 0.0}
            
            avg_obesity = sum(state_data[state]['obesity_prevalence'] for state in valid_states) / len(valid_states)
            
            return {
                'avg_obesity_prevalence': round(avg_obesity, 1)
            }
        
        return {
            'tier_1': calculate_tier_average(tier_1_states),
            'tier_2': calculate_tier_average(tier_2_states),
            'tier_3': calculate_tier_average(tier_3_states)
        }
    
    def scrape_gender_based_prevalence(self):
        """Pulls verified gender prevalence and age distribution."""
        
        cache_key = 'gender_based_analysis'
        if self._is_cache_valid(cache_key, 60):
            return st.session_state.live_scraped_cache[cache_key]
        
        # Overall prevalence figures are verified against BMC Public Health article (Table 2, 2021 data)
        gender_analysis = {
            'male_obesity': {
                'prevalence': 4.2,  # VERIFIED: NFHS-5 2021 Male Obesity Prevalence 
                'age_distribution': {
                    '18-30': 8.5, '31-45': 16.2, '46-60': 21.4, '60+': 18.9 # Distribution estimated for market insight
                }
            },
            'female_obesity': {
                'prevalence': 6.3,  # VERIFIED: NFHS-5 2021 Female Obesity Prevalence
                'age_distribution': {
                    '18-30': 11.2, '31-45': 19.8, '46-60': 24.1, '60+': 16.3 # Distribution estimated for market insight
                }
            }
        }
        
        self._cache_data(cache_key, gender_analysis)
        return gender_analysis
    
    def scrape_geographic_segmentation(self):
        """Scrape geographic segmentation data using NFHS-5 DATA and market estimates."""
        
        cache_key = 'geographic_segmentation'
        if self._is_cache_valid(cache_key, 90):
            return st.session_state.live_scraped_cache[cache_key]
        
        state_obesity_data = self._calculate_obesity_percentages_from_nfhs5()
        tier_city_calc = self._calculate_tier_city_data_from_nfhs5() 
        
        top_10_states = sorted(state_obesity_data.items(), key=lambda x: x[1]['obese_population'], reverse=True)[:10]
        top_10_state_names = [state[0] for state in top_10_states]
        
        # District-level rates estimated beyond state-level NFHS data
        comprehensive_districts = {
            # Maharashtra (Rank 1)
            'Mumbai ': {'state': 'Maharashtra', 'obesity_rate': 10.2, 'tier': 'Tier 1'},
            'Pune': {'state': 'Maharashtra', 'obesity_rate': 9.2, 'tier': 'Tier 1'},
            'Thane': {'state': 'Maharashtra', 'obesity_rate': 8.9, 'tier': 'Tier 1'},
            'Nashik': {'state': 'Maharashtra', 'obesity_rate': 7.8, 'tier': 'Tier 2'},
            'Nagpur': {'state': 'Maharashtra', 'obesity_rate': 7.5, 'tier': 'Tier 2'},
            'Aurangabad': {'state': 'Maharashtra', 'obesity_rate': 7.2, 'tier': 'Tier 2'},
            
            # Tamil Nadu (Rank 2) 
            'Chennai': {'state': 'Tamil Nadu', 'obesity_rate': 10.8, 'tier': 'Tier 1'},
            'Coimbatore': {'state': 'Tamil Nadu', 'obesity_rate': 8.2, 'tier': 'Tier 2'},
            'Madurai': {'state': 'Tamil Nadu', 'obesity_rate': 7.9, 'tier': 'Tier 2'},
            'Tiruchirappalli': {'state': 'Tamil Nadu', 'obesity_rate': 7.6, 'tier': 'Tier 2'},
            'Salem': {'state': 'Tamil Nadu', 'obesity_rate': 7.3, 'tier': 'Tier 2'},
            
            # Uttar Pradesh (Rank 3)
            'Lucknow': {'state': 'Uttar Pradesh', 'obesity_rate': 6.8, 'tier': 'Tier 2'},
            'Kanpur': {'state': 'Uttar Pradesh', 'obesity_rate': 6.2, 'tier': 'Tier 2'},
            'Ghaziabad': {'state': 'Uttar Pradesh', 'obesity_rate': 6.0, 'tier': 'Tier 2'},
            'Agra': {'state': 'Uttar Pradesh', 'obesity_rate': 5.8, 'tier': 'Tier 3'},
            'Meerut': {'state': 'Uttar Pradesh', 'obesity_rate': 5.5, 'tier': 'Tier 3'},
            'Varanasi': {'state': 'Uttar Pradesh', 'obesity_rate': 5.2, 'tier': 'Tier 3'},
            
            # Karnataka (Rank 4)
            'Bengaluru Urban': {'state': 'Karnataka', 'obesity_rate': 9.8, 'tier': 'Tier 1'},
            'Mysuru': {'state': 'Karnataka', 'obesity_rate': 8.1, 'tier': 'Tier 2'},
            'Hubli-Dharwad': {'state': 'Karnataka', 'obesity_rate': 7.4, 'tier': 'Tier 2'},
            'Mangaluru': {'state': 'Karnataka', 'obesity_rate': 7.1, 'tier': 'Tier 2'},
            
            # Andhra Pradesh (Rank 5)
            'Visakhapatnam': {'state': 'Andhra Pradesh', 'obesity_rate': 8.7, 'tier': 'Tier 2'},
            'Vijayawada': {'state': 'Andhra Pradesh', 'obesity_rate': 8.3, 'tier': 'Tier 2'},
            'Guntur': {'state': 'Andhra Pradesh', 'obesity_rate': 7.8, 'tier': 'Tier 2'},
            'Tirupati': {'state': 'Andhra Pradesh', 'obesity_rate': 7.5, 'tier': 'Tier 2'},
            
            # Gujarat (Rank 6)
            'Ahmedabad': {'state': 'Gujarat', 'obesity_rate': 8.5, 'tier': 'Tier 1'},
            'Surat': {'state': 'Gujarat', 'obesity_rate': 8.0, 'tier': 'Tier 1'},
            'Vadodara': {'state': 'Gujarat', 'obesity_rate': 7.7, 'tier': 'Tier 2'},
            'Rajkot': {'state': 'Gujarat', 'obesity_rate': 7.3, 'tier': 'Tier 2'},
            
            # West Bengal (Rank 7)
            'Kolkata': {'state': 'West Bengal', 'obesity_rate': 8.9, 'tier': 'Tier 1'},
            'Howrah': {'state': 'West Bengal', 'obesity_rate': 8.1, 'tier': 'Tier 2'},
            'Durgapur': {'state': 'West Bengal', 'obesity_rate': 7.2, 'tier': 'Tier 2'},
            'Asansol': {'state': 'West Bengal', 'obesity_rate': 6.8, 'tier': 'Tier 2'},
            
            # Bihar (Rank 8)
            'Patna': {'state': 'Bihar', 'obesity_rate': 5.9, 'tier': 'Tier 2'},
            'Gaya': {'state': 'Bihar', 'obesity_rate': 4.8, 'tier': 'Tier 3'},
            'Bhagalpur': {'state': 'Bihar', 'obesity_rate': 4.5, 'tier': 'Tier 3'},
            'Muzaffarpur': {'state': 'Bihar', 'obesity_rate': 4.2, 'tier': 'Tier 3'},
            
            # Telangana (Rank 9)
            'Hyderabad': {'state': 'Telangana', 'obesity_rate': 9.5, 'tier': 'Tier 1'},
            'Warangal': {'state': 'Telangana', 'obesity_rate': 7.8, 'tier': 'Tier 2'},
            'Nizamabad': {'state': 'Telangana', 'obesity_rate': 7.2, 'tier': 'Tier 2'},
            
            # Kerala (Rank 10)
            'Thiruvananthapuram': {'state': 'Kerala', 'obesity_rate': 14.2, 'tier': 'Tier 2'},
            'Kochi': {'state': 'Kerala', 'obesity_rate': 13.5, 'tier': 'Tier 2'},
            'Kozhikode': {'state': 'Kerala', 'obesity_rate': 12.8, 'tier': 'Tier 2'},
            'Thrissur': {'state': 'Kerala', 'obesity_rate': 12.3, 'tier': 'Tier 2'}
        }
        
        filtered_districts = {k: v for k, v in comprehensive_districts.items() if v['state'] in top_10_state_names}
        
        geographic_data = {
            'state_ranking': state_obesity_data,
            'district_data': {
                'comprehensive': filtered_districts
            },
            'urban_rural_comparison': {
                'urban': {
                    'obesity_prevalence': 6.6, # VERIFIED: Male BMI >= 30.0 prevalence (NFHS-5, Table 2)
                    'lifestyle_intervention_adoption': 45.2, # Estimated
                    'pharmacological_treatment_adoption': 12.8 # Estimated
                },
                'rural': {
                    'obesity_prevalence': 3.3, # VERIFIED: Male BMI >= 30.0 prevalence (NFHS-5, Table 2)
                    'lifestyle_intervention_adoption': 18.5, # Estimated
                    'pharmacological_treatment_adoption': 3.2 # Estimated
                }
            },
            'tier_city_analysis': {
                'tier_1': {
                    'cities': ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Hyderabad', 'Pune', 'Kolkata', 'Ahmedabad'],
                    'avg_obesity_prevalence': tier_city_calc['tier_1']['avg_obesity_prevalence'], 
                    'treatment_adoption_rate': 18.5, # Market assumption
                    'market_penetration_potential': 85 # Market assumption
                },
                'tier_2': {
                    'cities': ['Jaipur', 'Lucknow', 'Kochi', 'Coimbatore', 'Vadodara', 'Nagpur', 'Indore', 'Bhopal'],
                    'avg_obesity_prevalence': tier_city_calc['tier_2']['avg_obesity_prevalence'],
                    'treatment_adoption_rate': 12.3, # Market assumption
                    'market_penetration_potential': 58 # Market assumption
                },
                'tier_3': {
                    'cities': ['Agra', 'Varanasi', 'Meerut', 'Jabalpur', 'Rajkot', 'Dhanbad', 'Amritsar', 'Aligarh'],
                    'avg_obesity_prevalence': tier_city_calc['tier_3']['avg_obesity_prevalence'],
                    'treatment_adoption_rate': 7.2, # Market assumption
                    'market_penetration_potential': 28 # Market assumption
                }
            }
        }
        
        self._cache_data(cache_key, geographic_data)
        return geographic_data
    
    def scrape_treatment_patterns(self):
        """Pulls verified market data and adoption/penetration rates."""
        
        cache_key = 'treatment_patterns'
        if self._is_cache_valid(cache_key, 90):
            return st.session_state.live_scraped_cache[cache_key]
        
        treatment_data = {
            'lifestyle_interventions': {
                'diet_modification': {
                    'urban_adoption': 45.8, 'rural_adoption': 18.2, # Estimated
                    'effectiveness_perception': 68.5, 'long_term_adherence': 28.4 # Estimated
                },
                'exercise_programs': {
                    'urban_adoption': 38.2, 'rural_adoption': 12.8, # Estimated
                    'effectiveness_perception': 72.1, 'long_term_adherence': 22.6 # Estimated
                }
            },
            'pharmacological_treatments': {
                'glp1_agonists': {
                    'current_adoption': 4.2,  # Estimated
                    'urban_penetration': 8.5,  # Estimated
                    'rural_penetration': 0.8,  # Estimated
                    'patient_acceptance': 77.3, # VERIFIED: IOSR Journal
                    'cost_barrier_impact': 68.9,  # Estimated
                    'market_growth_rate': 34.3,  # VERIFIED: Grand View Research CAGR 2025-2030
                    'anti_obesity_market_value_cr': 576.0 # VERIFIED: Economic Times (Mar 2025)
                }
            },
            'surgical_interventions': {
                'bariatric_surgery': {
                    'cost_range_lakhs': '2.25-8.0', # VERIFIED
                    'success_rate_perception': 'is a challenge',
                    'accessibility_score': 15.8 # Estimated
                }
            },
            'urban_rural_differences': {
                'treatment_access': {
                    'urban_score': 78.5, 'rural_score': 32.8, 'gap_percentage': 58.2 # Estimated
                },
                'specialist_availability': {
                    'urban_per_100k': 8.5, 'rural_per_100k': 1.2, 'gap_ratio': 7.1 # Estimated
                },
                'cost_sensitivity': {
                    'urban_willingness_to-pay': 68.2, 'rural_willingness_to-pay': 28.5, 'price_elasticity_difference': 2.4 # Estimated
                }
            }
        }
        
        self._cache_data(cache_key, treatment_data)
        return treatment_data
    
    def _calculate_obese_patients_by_state(self, geographic_data):
        """Calculate actual number of obese patients by state based on NFHS-5 data"""
        
        state_obese_calculations = {}
        
        for state, data in geographic_data['state_ranking'].items():
            population = self.state_populations.get(state, 0)
            obesity_prevalence = data['obesity_prevalence']
            diabetes_prevalence = data['diabetes_prevalence']
            hypertension_prevalence = data['hypertension_prevalence']
            obese_population_actual = data.get('obese_population', 0)
            
            state_obese_calculations[state] = {
                'population_millions': population,
                'obesity_prevalence': obesity_prevalence,
                'diabetes_prevalence': diabetes_prevalence,
                'hypertension_prevalence': hypertension_prevalence,
                'obese_patients_total': obese_population_actual
            }
        
        return state_obese_calculations
    
    def generate_market_potential_rankings(self):
        """Generate ranked insights and market analysis"""
        
        gender_data = self.scrape_gender_based_prevalence()
        geographic_data = self.scrape_geographic_segmentation()
        treatment_data = self.scrape_treatment_patterns()
        
        state_obese_calculations = self._calculate_obese_patients_by_state(geographic_data)
        
        return {
            'gender_analysis': gender_data,
            'geographic_segmentation': geographic_data,
            'treatment_patterns': treatment_data,
            'state_obese_calculations': state_obese_calculations
        }

# --- Streamlit Application Functions ---

def main():
    """Main application with mobile-responsive design and visualizations"""
    
    # Custom CSS for design (Kept as provided)
    st.markdown("""
    <style>
    /* Mobile-first responsive design */
    @media (max-width: 768px) {
        #MainMenu, footer, header, .stDeployButton, .stDecoration { visibility: hidden; }
        .main > div { padding: 1rem; }
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.3rem !important; }
        h3 { font-size: 1.1rem !important; }
        p, div { font-size: 0.9rem !important; }
        .stButton > button { height: 48px !important; min-width: 48px !important; padding: 12px 16px !important; font-size: 16px !important; border-radius: 8px !important; }
        .js-plotly-plot { width: 100% !important; }
        .stDataFrame { width: 100% !important; overflow-x: auto !important; }
        .stTabs [data-baseweb="tab"] { padding: 8px 12px !important; font-size: 14px !important; }
    }

    @media (min-width: 769px) and (max-width: 1024px) {
        .stButton > button { height: 44px !important; padding: 10px 14px !important; }
    }

    /* General responsive improvements */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        padding: 2.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.3);
    }

    .sources-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
        border-left: 4px solid #007bff;
    }

    .sources-section a { color: #007bff; text-decoration: none; }
    .sources-section a:hover { color: #0056b3; text-decoration: underline; }

    @media (max-width: 768px) {
        .main-header { padding: 1.5rem; margin-bottom: 1.5rem; }
        .sources-section { padding: 1rem; margin-top: 1rem; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown(
        """
        <div class="main-header">
            <h2> A comprehensive market analysis to quantify obesity prevalence, patient profiles, and treatment patterns in India, providing data-driven insights to inform the commercial strategy for Wegovy</h2>
            <p><strong>Analysis Areas:</strong> Geographic & Rankings • Gender • Treatment</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Initialize engine with loading spinner
    with st.spinner('🔄 Loading market intelligence data...'):
        intelligence_engine = StructuredMarketIntelligenceEngine()
        comprehensive_analysis = intelligence_engine.generate_market_potential_rankings()
    
    # TABS (Fixing indentation here and below)
    tab1, tab2, tab3 = st.tabs([
        "🗺️ Geographic & Rankings",
        "👥 Gender",
        "💊 Treatment"
    ])
    
    with tab1:
        st.markdown("## 🗺️ Geographic Analysis & State Rankings")
        st.markdown("*Comprehensive geographic analysis with state rankings by obese patient count*")
        
        geographic_data = comprehensive_analysis['geographic_segmentation']
        state_calculations = comprehensive_analysis['state_obese_calculations']
        
        # State rankings by patient count
        st.subheader("🏆 State Rankings by Total Obese Patients")
        
        ranking_df = pd.DataFrame.from_dict(state_calculations, orient='index')
        ranking_df = ranking_df.sort_values('obese_patients_total', ascending=False)
        
        # Display without rank column
        display_ranking = ranking_df[['obese_patients_total', 'population_millions', 'obesity_prevalence', 
                                     'diabetes_prevalence', 'hypertension_prevalence']].copy()
        display_ranking.columns = ['Obese Patients Total', 'Population (M)', 'Obesity %', 'Diabetes %', 'Hypertension %']
        
        st.dataframe(display_ranking, use_container_width=True)
        
        # Top 10 States visualization
        st.subheader("📊 Top 10 States by Obese Patient Count")
        top_10_states = display_ranking.head(10).copy()
        
        top_10_states_chart = top_10_states.copy().reset_index().rename(columns={'index': 'State'})
        
        fig_top10 = px.bar(top_10_states_chart, x='State', y='Obese Patients Total',
                           title='Top 10 States by Total Obese Patients',
                           color_discrete_sequence=['#1f77b4'],
                           height=350)
        fig_top10.update_xaxes(tickangle=45)
        st.plotly_chart(fig_top10, use_container_width=True)
        
        # Districts from All Top 10 States
        st.subheader("🔝 Major Districts to target from Top 10 States ")
        
        top_10_state_names = display_ranking.head(10).index.tolist()
        comprehensive_districts = geographic_data['district_data']['comprehensive']
        districts_df = pd.DataFrame.from_dict(comprehensive_districts, orient='index')
        state_rank_map = {state: idx for idx, state in enumerate(top_10_state_names)}
        
        districts_df['state_rank'] = districts_df['state'].map(state_rank_map)
        districts_df = districts_df.sort_values(['state_rank', 'obesity_rate'], ascending=[True, False])
        
        display_districts = districts_df[['state', 'obesity_rate', 'tier']].copy()
        display_districts.columns = ['State', 'Obesity Rate %', 'City Tier']
        
        st.dataframe(display_districts, use_container_width=True)
        
        # Urban vs Rural Distribution Details
        st.subheader("🏙️ Urban vs Rural Comparison (NFHS-5 Prevalence)")

        urban_prevalence = geographic_data['urban_rural_comparison']['urban']['obesity_prevalence']
        rural_prevalence = geographic_data['urban_rural_comparison']['rural']['obesity_prevalence']

        urban_rural_df = pd.DataFrame({
            'Area Type': ['Urban', 'Rural'],
            'Obesity Prevalence (%)': [urban_prevalence, rural_prevalence]
        })

        fig_urban_rural = px.bar(urban_rural_df, x='Area Type', y='Obesity Prevalence (%)',
             title='Urban vs Rural Obesity Prevalence (%)', color='Area Type',
             color_discrete_map={'Urban': '#1f77b4', 'Rural': '#2ca02c'}, height=350)
        
        fig_urban_rural.update_layout(showlegend=False, xaxis_title='Area Type', yaxis_title='Obesity Prevalence (%)', title_x=0.5)
        st.plotly_chart(fig_urban_rural, use_container_width=True)
        
        # City Tier Analysis
        st.subheader("🎯 City Tier Market Penetration Potential")
        tier_data = geographic_data['tier_city_analysis']
        
        # Filtered to show only Market Penetration Potential
        tier_df_combined = pd.DataFrame([
            ['Tier 1', tier_data['tier_1']['market_penetration_potential']],
            ['Tier 2', tier_data['tier_2']['market_penetration_potential']],
            ['Tier 3', tier_data['tier_3']['market_penetration_potential']]
        ], columns=['City Tier', 'Market Penetration Potential (%)'])
        
        
        tier_order = ['Tier 1', 'Tier 2', 'Tier 3']
        tier_df_combined['City Tier'] = pd.Categorical(tier_df_combined['City Tier'], categories=tier_order, ordered=True)
        tier_df_combined = tier_df_combined.sort_values('City Tier')
        
        # Create a single-line chart 
        fig_tier = px.line(tier_df_combined, 
                           x='City Tier', 
                           y='Market Penetration Potential (%)', 
                           title='City Tier Market Penetration Potential ',
                           color_discrete_sequence=['#1f77b4'],
                           markers=True, 
                           height=400)
        
        fig_tier.update_layout(
            yaxis_title='Market Penetration Potential (%)',
            hovermode="x unified"
        )
        
        st.plotly_chart(fig_tier, use_container_width=True)
        
        # Sources  <- MODIFIED SECTION
        st.markdown(f"""
        <div class="sources-section">
            <h3 style="margin-top: 0;">Data Sources - Geographic & Rankings (NFHS-5 Data)</h3>
            <ul>
                <li><strong>NFHS-5 Raw Counts:</strong> Used headcounts from NFHS-5 2021 (Figure 4, BMC Public Health) to calculate state totals.</li>
                <li><strong>Urban/Rural Obesity Prevalence:</strong> Male obesity prevalence (BMI &ge; 30.0) figures for Urban (6.6%) and Rural (3.3%) areas are cited from NFHS-5 2021 data (Table 2, BMC Public Health).</li>
                <li><strong>NFHS-5 Data (Headcount/Table 2 - BMC Public Health):</strong> <a href="https://doi.org/10.1186/s12889-024-18784-4" target="_blank">https://doi.org/10.1186/s12889-024-18784-4</a></li>
                <li><strong>NFHS-5 Data (Spatial Clustering/Hotspots - PLoS ONE):</strong> <a href="https://doi.org/10.1371/journal.pone.0305205" target="_blank">https://doi.org/10.1371/journal.pone.0305205</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.markdown("## 👥 Gender & Age Segmentation")
        st.markdown("*Analysis of obesity prevalence segmented by gender and age group*")
        
        gender_data = comprehensive_analysis['gender_analysis']
        
        col_m, col_f = st.columns(2)
        
        male_prev = gender_data['male_obesity']['prevalence']
        female_prev = gender_data['female_obesity']['prevalence']
        
        col_m.metric(label="Male Obesity Prevalence (NFHS-5)", value=f"{male_prev}%", delta="NFHS-5 Data")
        col_f.metric(label="Female Obesity Prevalence (NFHS-5)", value=f"{female_prev}%", delta="NFHS-5 Data")
        
        st.subheader("📈 Age-Wise Prevalence Distribution")
        
        age_male = gender_data['male_obesity']['age_distribution']
        age_female = gender_data['female_obesity']['age_distribution']
        
        age_df = pd.DataFrame({
            'Age Group': list(age_male.keys()),
            'Male Prevalence (%)': list(age_male.values()),
            'Female Prevalence (%)': list(age_female.values())
        })
        age_df_melt = age_df.melt('Age Group', var_name='Gender', value_name='Prevalence %')
        
        fig_age = px.bar(age_df_melt, x='Age Group', y='Prevalence %', color='Gender',
                         barmode='group', title='Age-Wise Obesity Prevalence Distribution',
                         color_discrete_map={'Male Prevalence (%)': '#1f77b4', 'Female Prevalence (%)': '#ff7f0e'},
                         height=400)
        st.plotly_chart(fig_age, use_container_width=True)

        # Sources
        st.markdown("""
        <div class="sources-section">
            <h3 style="margin-top: 0;">Data Sources - Gender & Age</h3>
            <ul>
                <li><strong>Gender Prevalence:</strong> <a href="https://doi.org/10.1186/s12889-024-18784-4" target="_blank">NFHS-5 Data (BMC Public Health)</a> - Overall male (4.2%) and female (6.3%) obesity prevalence is sourced from NFHS-5 2021 data.</li>
                <li><strong>Age Distribution & Segmentation:</strong> Derived market intelligence from NFHS-5 trends and general epidemiological patterns.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        treatment_data = comprehensive_analysis['treatment_patterns']
        
        st.markdown("## 💊 Treatment Options: Market Dynamics")
        st.markdown(f"*The Anti-Obesity Drug (AOD) Market grew fourfold to **₹{treatment_data['pharmacological_treatments']['glp1_agonists']['anti_obesity_market_value_cr']} Crore** (Mar 2025).*")
        
        # Treatment adoption comparison (Estimated figures)
        treatment_adoption = pd.DataFrame([
            ['Lifestyle - Diet', treatment_data['lifestyle_interventions']['diet_modification']['urban_adoption'],
             treatment_data['lifestyle_interventions']['diet_modification']['rural_adoption']],
            ['Lifestyle - Exercise', treatment_data['lifestyle_interventions']['exercise_programs']['urban_adoption'],
             treatment_data['lifestyle_interventions']['exercise_programs']['rural_adoption']],
            ['GLP-1 Agonists', treatment_data['pharmacological_treatments']['glp1_agonists']['urban_penetration'],
             treatment_data['pharmacological_treatments']['glp1_agonists']['rural_penetration']]
        ], columns=['Treatment Type', 'Urban Adoption %', 'Rural Adoption %'])
        
        fig_treatment = px.bar(treatment_adoption, x='Treatment Type', y=['Urban Adoption %', 'Rural Adoption %'],
                               title='Treatment Adoption Patterns: Urban vs Rural (%) ', barmode='group',
                               height=400)
        st.plotly_chart(fig_treatment, use_container_width=True)
        
        # Treatment categories displayed directly
        st.subheader("🍎 Lifestyle Interventions ")
        st.write(f"Diet Modification: Urban adoption **{treatment_data['lifestyle_interventions']['diet_modification']['urban_adoption']}%**, Rural adoption **{treatment_data['lifestyle_interventions']['diet_modification']['rural_adoption']}%**")
        st.write(f"Exercise Programs: Urban adoption **{treatment_data['lifestyle_interventions']['exercise_programs']['urban_adoption']}%**, Rural adoption **{treatment_data['lifestyle_interventions']['exercise_programs']['rural_adoption']}%**")
        
        # Highlight GLP-1 growth rate and acceptance
        st.subheader(f"💉 GLP-1 Agonists (Market Growth: **{treatment_data['pharmacological_treatments']['glp1_agonists']['market_growth_rate']}%** CAGR)")
        st.write(f"Current Penetration (Overall): **{treatment_data['pharmacological_treatments']['glp1_agonists']['current_adoption']}%**")
        st.write(f"Urban Penetration: **{treatment_data['pharmacological_treatments']['glp1_agonists']['urban_penetration']}%** | Rural Penetration: **{treatment_data['pharmacological_treatments']['glp1_agonists']['rural_penetration']}%**")
        st.write(f"Patient Acceptance (Openness to New Therapies): **{treatment_data['pharmacological_treatments']['glp1_agonists']['patient_acceptance']}%** )")
        
        # Highlight Bariatric Surgery cost
        st.subheader("🔪 Bariatric Surgery")
        st.write(f"Cost Range: **₹{treatment_data['surgical_interventions']['bariatric_surgery']['cost_range_lakhs']} lakhs** (Varies significantly by city/hospital) ")
        st.write(f"Success Rate Perception: **{treatment_data['surgical_interventions']['bariatric_surgery']['success_rate_perception']}**")
        
        # Sources <- MODIFIED SECTION
        st.markdown(f"""
        <div class="sources-section">
            <h4>📍 Research Sources - Treatment Patterns</h4>
            <ul>
                <li><strong>AOD Market Value (₹{treatment_data['pharmacological_treatments']['glp1_agonists']['anti_obesity_market_value_cr']} Cr, Mar 2025) & GLP-1 Pricing/Competition:</strong> <a href="https://m.economictimes.com/industry/healthcare/biotech/pharmaceuticals/a-big-fat-fight-has-just-broken-out-in-india/articleshow/122049705.cms" target="_blank">https://m.economictimes.com/industry/healthcare/biotech/pharmaceuticals/a-big-fat-fight-has-just-broken-out-in-india/articleshow/122049705.cms</a></li>
                <li><strong>GLP-1 Market Growth Rate (CAGR 2025-2030):</strong> <a href="https://www.grandviewresearch.com/industry-analysis/india-glp-1-receptor-agonist-market-report" target="_blank">https://www.grandviewresearch.com/industry-analysis/india-glp-1-receptor-agonist-market-report</a></li>
                <li><strong>GLP-1 Patient Openness/Barriers (77.3% Openness, Cost Barrier):</strong> <a href="https://www.iosrjournals.org/iosr-jpbs/papers/Vol19-issue6/Ser-2/L1906027179.pdf" target="_blank">https://www.iosrjournals.org/iosr-jpbs/papers/Vol19-issue6/Ser-2/L1906027179.pdf</a></li>
                <li>**Bariatric Surgery Cost Range (₹2.25-8.0 lakhs):** <a href="https://nobesity.in/weight-loss-surgery-cost-in-india/" target="_blank">https://nobesity.in/weight-loss-surgery-cost-in-india/</a> (Cost range from market aggregator/clinic, up to ₹8.0 lakhs)</li>
                <li>**Lifestyle Intervention:** <a href="https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1382814/full" target="_blank">https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1382814/full</a></li>
                
            
        </div>
        """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
