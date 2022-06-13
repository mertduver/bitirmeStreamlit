import streamlit as st
from PIL import Image


def show_home_page():
    st.title("Home Page")
    st.header("""Health Care & Diabetes""")
    st.markdown("***")
    col1, col2 = st.columns([2,1])
    # col1.write("In the present day, healthcare has come to mean every aspect, service and device for taking care of your health.  It has become conscripted by government, politicians, political ideologues, third parties and media to conveniently and neatly define whatever they want to “give” you. By simply becoming involved, these middlemen are diluting the quality of the actual health service you can achieve, be they government or insurers. I challenge the notion that healthcare is an entity that can be confined to one simplistic model. Healthcare is not a thing at all to be given, bought or sold, but an entire ecosystem with many unique moving parts that are only connected by virtue of the existence of the patients. Each patient, having individual needs, will have a landscape that suits the needs of their own health, and one that will change with time. While Americans have a need of good health, they have a right to choose the ecosystem that suits their own needs. The larger healthcare landscape includes all goods, services, and payment mechanisms for achieving and maintaining one’s health. It includes, but is not limited to: physician offices, hospitals, labs, radiology centers, physical therapy offices, pharmaceutical companies, pharmacies, and now health insurance companies, group purchasing organizations, pharmacy benefit managers, corporate healthcare systems, and combinations of insurance/PBM/pharmacy and much more. All of these entities are not necessary in each healthcare interaction for a patient. In 100 percent of interactions, insurance has inserted itself. For simpler interactions, insurance serves to keep costs hidden and high.  ")
    col1.header("What is Health Care")
    col1.write("Health care or healthcare is the maintenance or improvement of health via the prevention, diagnosis, treatment, amelioration, or cure of disease, illness, injury, and other physical and mental impairments in people. Health care is delivered by health professionals and allied health fields. Medicine, dentistry, pharmacy, midwifery, nursing, optometry, audiology, psychology, occupational therapy, physical therapy, athletic training, and other health professions are all part of health care. It includes work done in providing primary care, secondary care, and tertiary care, as well as in public health.")
    col1.header("What is Diabetes")
    col1.write("Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces. Insulin is a hormone that regulates blood sugar. Hyperglycaemia, or raised blood sugar, is a common effect of uncontrolled diabetes and over time leads to serious damage to many of the body's systems, especially the nerves and blood vessels.")
    image = Image.open('./images/health1.jpg')

    col2.image(image)
    # st.image(image, caption='Sunrise by the mountains')