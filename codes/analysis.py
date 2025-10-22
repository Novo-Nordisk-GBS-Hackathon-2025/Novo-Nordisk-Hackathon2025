import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Wegovy Comprehensive Market Analysis for strategies",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🎯"
)

class StructuredMarketIntelligenceEngine:
    """Comprehensive market intelligence engine for Wegovy India."""
    
    def __init__(self):
        # State Populations (in millions) - Source: Census 2011
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
        
        # NFHS-5 BMI DATA - Source: BMC Public Health 2024
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
            'Jammu and Kashmir': {'severely_moderately_thin': 55600, 'mildly_thin': 136214, 'normal': 4720630, 'overweight': 23628, 'obese': 58976},
            'Mizoram': {'severely_moderately_thin': 4477, 'mildly_thin': 20066, 'normal': 447596, 'overweight': 199545, 'obese': 43181},
            'Meghalaya': {'severely_moderately_thin': 33462, 'mildly_thin': 105038, 'normal': 1523920, 'overweight': 292010, 'obese': 35516},
            'Nagaland': {'severely_moderately_thin': 15576, 'mildly_thin': 37144, 'normal': 714911, 'overweight': 228433, 'obese': 31927},
            'Sikkim': {'severely_moderately_thin': 4201, 'mildly_thin': 6013, 'normal': 247273, 'overweight': 135334, 'obese': 26092}
        }
        
        self.comprehensive_sources = {
            'nfhs5_data': {
                'https://doi.org/10.1186/s12889-024-18784-4': {
                    'title': 'Temporal change in prevalence of BMI categories in India: patterns across States and Union territories of India, 1999–2021',
                    'journal': 'BMC Public Health',
                    'year': 2024
                },
                'https://doi.org/10.1371/journal.pone.0305205': {
                    'title': 'Spatial clustering of overweight/obesity among women in India: Insights from the latest National Family Health Survey',
                    'journal': 'PLoS ONE',
                    'year': 2024
                },
            },
            'treatment_patterns': {
                'https://www.grandviewresearch.com/industry-analysis/india-glp-1-receptor-agonist-market-report': {
                    'title': 'India GLP-1 Receptor Agonist Market Report',
                    'source': 'Grand View Research'
                },
                'https://m.economictimes.com/industry/healthcare/biotech/pharmaceuticals/a-big-fat-fight-has-just-broken-out-in-india/articleshow/122049705.cms': {
                    'title': 'Anti-Obesity Drug Market Analysis',
                    'source': 'Economic Times',
                    'year': 2025
                },
                'https://www.iosrjournals.org/iosr-jpbs/papers/Vol19-issue6/Ser-2/L1906027179.pdf': {
                    'title': 'Patient Acceptance of Obesity Therapies',
                    'source': 'IOSR Journal'
                },
                'https://nobesity.in/weight-loss-surgery-cost-in-india/': {
                    'title': 'Bariatric Surgery Cost in India',
                    'source': 'Nobesity India'
                },
                'https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1382814/full': {
                    'title': 'Lifestyle Interventions for Obesity',
                    'source': 'Frontiers in Endocrinology',
                    'year': 2024
                },
            }
        }
    
    def _calculate_obesity_percentages_from_nfhs5(self):
        """Calculate obesity percentages and estimate comorbidities from NFHS-5 data"""
        state_obesity_data = {}
        
        for state, data in self.nfhs5_bmi_data.items():
            if state == 'India':
                continue
                
            total_population = sum(data.values())
            if total_population == 0:
                continue

            obesity_percentage = (data['obese'] / total_population) * 100
            diabetes_percentage = obesity_percentage * 2.1 
            hypertension_percentage = obesity_percentage * 2.3 
            
            state_obesity_data[state] = {
                'obesity_prevalence': round(obesity_percentage, 1),
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
        
        tier_city_calc = {
            'tier_1': calculate_tier_average(tier_1_states),
            'tier_2': calculate_tier_average(tier_2_states),
            'tier_3': calculate_tier_average(tier_3_states)
        }

        # Market penetration potential based on healthcare access and economic factors
        # Tier 1: 85%, Tier 2: 60%, Tier 3: 35%
        return {
            'tier_1': {
                'avg_obesity_prevalence': tier_city_calc['tier_1']['avg_obesity_prevalence'],
                'market_penetration_potential': 85
            },
            'tier_2': {
                'avg_obesity_prevalence': tier_city_calc['tier_2']['avg_obesity_prevalence'],
                'market_penetration_potential': 60
            },
            'tier_3': {
                'avg_obesity_prevalence': tier_city_calc['tier_3']['avg_obesity_prevalence'],
                'market_penetration_potential': 35
            }
        }
    
    def scrape_gender_based_prevalence(self):
        """ gender prevalence and age distribution."""
        
        gender_analysis = {
            'male_obesity': {
                'prevalence': 4.2,
                'age_distribution': {
                    '18-30': 8.5, '31-45': 16.2, '46-60': 21.4, '60+': 18.9
                }
            },
            'female_obesity': {
                'prevalence': 6.3,
                'age_distribution': {
                    '18-30': 11.2, '31-45': 19.8, '46-60': 24.1, '60+': 16.3
                }
            }
        }
        
        return gender_analysis
    
    def scrape_geographic_segmentation(self):
        """Scrape geographic segmentation data using NFHS-5 DATA and market estimates."""
        
        state_obesity_data = self._calculate_obesity_percentages_from_nfhs5()
        tier_city_calc = self._calculate_tier_city_data_from_nfhs5() 
        
        top_10_states = sorted(state_obesity_data.items(), key=lambda x: x[1]['obese_population'], reverse=True)[:10]
        top_10_state_names = [state[0] for state in top_10_states]
        
        districts_from_paper = {
            'Kanniyakumari': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Coimbatore': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Thiruvallur': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Kancheepuram': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Vellore': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Tiruppur': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Namakkal': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Chennai': {'state': 'Tamil Nadu', 'tier': 'Tier 1'},
            'Theni': {'state': 'Tamil Nadu', 'tier': 'Tier 3'},
            'Thanjavur': {'state': 'Tamil Nadu', 'tier': 'Tier 3'},
            'Thoothukkudi': {'state': 'Tamil Nadu', 'tier': 'Tier 3'},
            'Madurai': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Erode': {'state': 'Tamil Nadu', 'tier': 'Tier 2'},
            'Thiruvananthapuram': {'state': 'Kerala', 'tier': 'Tier 2'},
            'Kollam': {'state': 'Kerala', 'tier': 'Tier 3'},
            'Pathanamthitta': {'state': 'Kerala', 'tier': 'Tier 3'},
            'Thrissur': {'state': 'Kerala', 'tier': 'Tier 2'},
            'Alappuzha': {'state': 'Kerala', 'tier': 'Tier 3'},
            'Kottayam': {'state': 'Kerala', 'tier': 'Tier 3'},
            'Guntur': {'state': 'Andhra Pradesh', 'tier': 'Tier 2'},
            'West Godavari': {'state': 'Andhra Pradesh', 'tier': 'Tier 3'},
            'East Godavari': {'state': 'Andhra Pradesh', 'tier': 'Tier 3'},
            'Krishna': {'state': 'Andhra Pradesh', 'tier': 'Tier 3'},
            'Hyderabad': {'state': 'Telangana', 'tier': 'Tier 1'},
            'Medchal-Malkajgiri': {'state': 'Telangana', 'tier': 'Tier 2'},
            'Sahibzada Ajit Singh': {'state': 'Punjab', 'tier': 'Tier 2'},
            'Jalandhar': {'state': 'Punjab', 'tier': 'Tier 2'},
            'Fatehgarh Sahib': {'state': 'Punjab', 'tier': 'Tier 3'},
            'Ludhiana': {'state': 'Punjab', 'tier': 'Tier 2'},
            'Rupnagar': {'state': 'Punjab', 'tier': 'Tier 3'},
            'Patiala': {'state': 'Punjab', 'tier': 'Tier 2'},
            'Kapurthala': {'state': 'Punjab', 'tier': 'Tier 3'},
            'Shahid Bhagat Singh Nagar': {'state': 'Punjab', 'tier': 'Tier 3'},
            'Amritsar': {'state': 'Punjab', 'tier': 'Tier 2'},
            'Hoshiarpur': {'state': 'Punjab', 'tier': 'Tier 3'},
            'Jhajjar': {'state': 'Haryana', 'tier': 'Tier 3'},
            'Ambala': {'state': 'Haryana', 'tier': 'Tier 2'},
            'Panchkula': {'state': 'Haryana', 'tier': 'Tier 2'},
            'Kachchh': {'state': 'Gujarat', 'tier': 'Tier 3'},
            'Dhule': {'state': 'Maharashtra', 'tier': 'Tier 3'},
            'Jalgaon': {'state': 'Maharashtra', 'tier': 'Tier 3'}
        }
        
        filtered_districts = {k: v for k, v in districts_from_paper.items() if v['state'] in top_10_state_names}
        
        geographic_data = {
            'state_ranking': state_obesity_data,
            'district_data': {
                'comprehensive': filtered_districts
            },
            'urban_rural_comparison': {
                'urban': {'obesity_prevalence': 6.6},
                'rural': {'obesity_prevalence': 3.3}
            },
            'tier_city_analysis': self._calculate_tier_city_data_from_nfhs5()
        }
        
        return geographic_data
    
    def scrape_treatment_patterns(self):
        
        treatment_data = {
            'lifestyle_interventions': {
                 'source_basis': 'https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2024.1382814/full' 
            },
            'pharmacological_treatments': {
                'glp1_agonists': {
                    'patient_acceptance': 77.3,
                    'market_growth_rate': 34.3,
                    'anti_obesity_market_value_cr': 576.0
                }
            },
            'surgical_interventions': {
                'bariatric_surgery': {
                    'cost_range_lakhs': '2.25-8.0',
                }
            },
        }
        
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

def main():
    """Main application with mobile-responsive design and visualizations"""
    
    intelligence_engine = StructuredMarketIntelligenceEngine()

    st.markdown("""
    <style>
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

    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        padding: 2.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.3);
    }

    @media (max-width: 768px) {
        .main-header { padding: 1.5rem; margin-bottom: 1.5rem; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="main-header">
            <h2>A comprehensive market analysis to quantify obesity prevalence, patient profiles, and treatment patterns in India, providing data-driven insights to inform the commercial strategy for Wegovy</h2>
            <p><strong>Analysis Areas:</strong> Geographic & Rankings • Gender • Treatment</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.spinner('🔄 Loading market intelligence data...'):
        comprehensive_analysis = intelligence_engine.generate_market_potential_rankings()
    
    tab1, tab2, tab3 = st.tabs([
        "🗺️ Geographic & Rankings",
        "👥 Gender",
        "💊 Treatment"
    ])

    nfhs_sources = intelligence_engine.comprehensive_sources['nfhs5_data']
    treatment_sources = intelligence_engine.comprehensive_sources['treatment_patterns']

    with tab1:
        st.markdown("## 🗺️ Geographic Analysis & State Rankings")
        st.markdown("*Comprehensive geographic analysis with state rankings by obese patient count*")
        
        geographic_data = comprehensive_analysis['geographic_segmentation']
        state_calculations = comprehensive_analysis['state_obese_calculations']
        
        st.subheader("🏆 State Rankings by Total Obese Patients")
        
        ranking_df = pd.DataFrame.from_dict(state_calculations, orient='index')
        ranking_df = ranking_df.sort_values('obese_patients_total', ascending=False)
        
        display_ranking = ranking_df[['obese_patients_total', 'obesity_prevalence']].copy()
        display_ranking.columns = ['Obese Patients Total', 'Obesity %']
        
        st.dataframe(display_ranking, use_container_width=True)
        
        st.write("**Diabetes and hypertension are critical comorbidities that drive the therapeutic market for anti-obesity medications like Wegovy.**")
        
        st.subheader("📊 Top 10 States by Obese Patient Count")
        top_10_states = display_ranking.head(10).copy()
        
        top_10_states_chart = top_10_states.copy().reset_index().rename(columns={'index': 'State'})
        
        fig_top10 = px.bar(top_10_states_chart, x='State', y='Obese Patients Total',
                           title='Top 10 States by Total Obese Patients',
                           color_discrete_sequence=['#1f77b4'],
                           height=350)
        fig_top10.update_xaxes(tickangle=45)
        st.plotly_chart(fig_top10, use_container_width=True)
        
        st.subheader("🔝 Major Districts to Target from Top 10 States")
        
        top_10_state_names = display_ranking.head(10).index.tolist()
        districts_from_paper = geographic_data['district_data']['comprehensive']
        districts_df = pd.DataFrame.from_dict(districts_from_paper, orient='index')
        state_rank_map = {state: idx for idx, state in enumerate(top_10_state_names)}
        
        districts_df['state_rank'] = districts_df['state'].map(state_rank_map)
        districts_df = districts_df.sort_values(['state_rank', 'state'], ascending=[True, True])
        
        display_districts = districts_df[['state', 'tier']].copy()
        display_districts.columns = ['State', 'City Tier']
        
        st.dataframe(display_districts, use_container_width=True)
    
        
        st.subheader("🏙️ Urban vs Rural Comparison")

        urban_prevalence = geographic_data['urban_rural_comparison']['urban']['obesity_prevalence']
        rural_prevalence = geographic_data['urban_rural_comparison']['rural']['obesity_prevalence']

        urban_rural_df = pd.DataFrame({
            'Area Type': ['Urban', 'Rural'],
            'Obesity Prevalence (%)': [urban_prevalence, rural_prevalence]
        })

        fig_urban_rural = px.bar(urban_rural_df, x='Area Type', y='Obesity Prevalence (%)',
             title='Urban vs Rural Obesity Prevalence (NFHS-5)', color='Area Type',
             color_discrete_map={'Urban': '#1f77b4', 'Rural': '#2ca02c'}, height=350)
        
        fig_urban_rural.update_layout(showlegend=False, xaxis_title='Area Type', yaxis_title='Obesity Prevalence (%)', title_x=0.5)
        st.plotly_chart(fig_urban_rural, use_container_width=True)
        
        st.subheader("🎯 City Tier Market Penetration Potential")
        tier_data = geographic_data['tier_city_analysis']
        
        tier_df_combined = pd.DataFrame([
            ['Tier 1', tier_data['tier_1']['market_penetration_potential']],
            ['Tier 2', tier_data['tier_2']['market_penetration_potential']],
            ['Tier 3', tier_data['tier_3']['market_penetration_potential']]
        ], columns=['City Tier', 'Market Penetration Potential (%)'])
        
        tier_order = ['Tier 1', 'Tier 2', 'Tier 3']
        tier_df_combined['City Tier'] = pd.Categorical(tier_df_combined['City Tier'], categories=tier_order, ordered=True)
        tier_df_combined = tier_df_combined.sort_values('City Tier')
        
        fig_tier = px.bar(tier_df_combined, 
                          x='City Tier', 
                          y='Market Penetration Potential (%)', 
                          title='City Tier Market Penetration Potential', 
                          color_discrete_sequence=['#1f77b4'],
                          height=400,
                          text='Market Penetration Potential (%)')
        
        fig_tier.update_traces(texttemplate='%{text}%', textposition='outside')
        fig_tier.update_layout(
            yaxis_title='Market Penetration Potential (%)',
            xaxis_title='City Tier',
            yaxis_range=[0, 100]
        )
        
        st.plotly_chart(fig_tier, use_container_width=True)
        
        
        # SOURCES SECTION - STREAMLIT NATIVE
        st.markdown("---")
        st.subheader("📚 Data Sources - Geographic & Rankings")
        
        with st.expander("**NFHS-5 Data Sources**", expanded=False):
            for url, meta in nfhs_sources.items():
                st.markdown(f"**{meta['title']}**")
                st.markdown(f"*{meta['journal']}, {meta['year']}*")
                st.markdown(f"[{url}]({url})")
                st.markdown("")
        
        with st.expander("**Market Assumptions & Estimates**", expanded=False):
            st.markdown("**State Population Figures:** Census 2011")
            st.markdown("")
            
            st.markdown("**Comorbidity Multipliers (Diabetes 2.1×, Hypertension 2.3×):**")
            st.markdown("- [Das et al., 2022 - Association of overweight and obesity with hypertension, diabetes and comorbidity](https://bmjopen.bmj.com/content/12/7/e052822)")
            st.markdown("- [Yamada et al., 2023 - Obesity and risk for its comorbidities](https://www.nature.com/articles/s41598-023-29276-7)")
            st.markdown("")
            
            st.markdown("**City Tier Classification:**")
            st.markdown("- [Decoding Indian Cities Classifications (UP Investment Portal)](https://invest.up.gov.in/wp-content/uploads/2023/06/decoding_270623.pdf)")
            st.markdown("- [Understanding Indian city classification (360 Realtors, 2024)](https://www.360realtors.com/blog/post/understanding-indian-city-classification-in-tier-i-ii-iii-and-iv-blid749)")
            st.markdown("")
            
            st.markdown("**Market Penetration Potential:**")
            st.markdown("- [Marketing Healthcare Services in Tier 2 & 3 Cities (SocialChamps, 2025)](https://socialchamps.com/marketing-healthcare-services-in-tier-2-3-indian-cities-strategies-for-2025/)")
            st.markdown("- [Transforming healthcare in tier 2 & 3 cities (Express Healthcare, 2024)](https://www.expresshealthcare.in/news/transforming-healthcare-in-tier-2-tier-3-cities-with-health-it/447241/)")
            st.markdown("- [Health Insurance Coverage in India (Ministry of Health & Family Welfare)](https://prc.mohfw.gov.in/fileDownload?fileName=Health+Insurance+Coverage+in+India+Insights+for+National+Health+Protection+Scheme.pdf)")
        
        st.caption("**Applicable to:** State obesity prevalence, district hotspots, urban/rural comparison, comorbidity estimates, city tier assignments, market penetration")
        
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
        

        # SOURCES SECTION - STREAMLIT NATIVE
        st.markdown("---")
        st.subheader("📚 Data Sources - Gender & Age")
        
        with st.expander("**Gender Obesity Prevalence**", expanded=False):
            meta = list(nfhs_sources.values())[0]
            st.markdown(f"**{meta['title']}**")
            st.markdown(f"*{meta['journal']}, {meta['year']}*")
            st.markdown(f"[{list(nfhs_sources.keys())[0]}]({list(nfhs_sources.keys())[0]})")
            st.markdown("")
            st.markdown("**Data:** Male 4.2%, Female 6.3% (Table 2)")
        
        with st.expander("**Age-Wise Distribution**", expanded=False):
            st.markdown("**Source:** General epidemiological patterns and NFHS-5 trends")

        
        st.caption("**Applicable to:** Gender-specific prevalence, Age-group distribution")

    with tab3:
        treatment_data = comprehensive_analysis['treatment_patterns']

        st.markdown("## 💊 Treatment Options: Market Dynamics")
        st.markdown(f"*The Anti-Obesity Drug (AOD) Market grew fourfold to **₹{treatment_data['pharmacological_treatments']['glp1_agonists']['anti_obesity_market_value_cr']} Crore** (Mar 2025).*")
        
        st.subheader("🍎 Lifestyle Interventions")
        st.markdown("""**Comprehensive lifestyle interventions** are the **foundational treatment** for obesity which includes diet, exercise, behavioral therapy, etc.""")
        
        st.subheader(f"💉 GLP-1 Agonists (Market Growth: **{treatment_data['pharmacological_treatments']['glp1_agonists']['market_growth_rate']}%** CAGR)")
        st.write(f"Patient Acceptance (Openness to New Therapies): **{treatment_data['pharmacological_treatments']['glp1_agonists']['patient_acceptance']}%**")
        
        st.subheader("🔪 Bariatric Surgery")
        st.write(f"Cost Range: **₹{treatment_data['surgical_interventions']['bariatric_surgery']['cost_range_lakhs']} lakhs**")
        
        # SOURCES SECTION - STREAMLIT NATIVE
        st.markdown("---")
        st.subheader("📚 Research Sources - Treatment Patterns")
        
        with st.expander("**Treatment Market Data**", expanded=False):
            for url, meta in treatment_sources.items():
                st.markdown(f"**{meta['title']}**")
                source_text = f"*{meta['source']}"
                if 'year' in meta:
                    source_text += f", {meta['year']}"
                source_text += "*"
                st.markdown(source_text)
                st.markdown(f"[{url}]({url})")
                st.markdown("")
        
        st.caption("**Applicable to:** AOD market value, GLP-1 growth rate, patient acceptance, surgery costs, lifestyle intervention clinical basis")


if __name__ == '__main__':
    main()
