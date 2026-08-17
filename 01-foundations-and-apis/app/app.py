import httpx
import streamlit as st

# titulo y descripcion de pagina
st.title("Web Scraper")
st.set_page_config(page_icon = "A")

st.write("Enter a URL to extract and process its content.")

# campo de entrada para la URL
url_input = st.text_input(
    label="URL Address",
    placeholder="https://example.com",
)

# Boton
if st.button("Scrape URL"):
    if not url_input:
        st.warning("Please enter a URL.")
    else:
        with st.spinner("Scraping webpage..."):
            try:
                # peticion a FastApi al endpoint post scrape 
                response = httpx.post(
                    "http://127.0.0.1:8000/scrape",
                    json={"url": url_input},
                )

                if response.status_code != 200:
                    st.error(f"Error {response.status_code} from server:")
                    st.json(response.json())
                    st.stop()

                # respuesta de FastApi 200 ok 
                st.success("Scraping completed successfully")
                st.json(response.json())
                    

            # manejo extra de excepciones 
            
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")