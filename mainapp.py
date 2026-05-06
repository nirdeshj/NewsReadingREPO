import streamlit as st
import userinput
import mainread


def get_user_input(ut):
    usertopiclist = userinput.main(ut)
    return usertopiclist

def fetch_news(topiclist):
    return mainread.main(topiclist)

def app_ui():
    st.set_page_config(page_title = 'TOP NEWS', page_icon="🧊", layout = 'centered')
    st.title('Today\'s news', text_alignment = 'center')
    print('\n')
    user_topic = st.text_input("", placeholder="Enter topics separated by comma (eg: technology, liverpool fc, politics)")
    article_data = {}
    num_articles = st.slider("Maximum number of articles per topic", min_value=1, max_value=mainread.MAX_NO_OF_ARTICLES, value=5, step=1)
    if (st.button('Get my news', key='newsfetch', help='Fetch latest news from your topics', type="primary")):
       if user_topic == "":
           st.warning("No topic entered. Can't fetch news.")
           return 
       user_topic_list = get_user_input(user_topic)
       article_data = fetch_news(user_topic_list)
       display_news(article_data, num_articles)

def display_news(adata, num):
    cols = st.columns(1 if len(adata) == 1 else 2, border = True, gap = 'large', width = 'stretch')
    col1 = cols[0]
    col2 = cols[1] if len(cols) > 1 else None

    for i, topic in enumerate(adata):
        col = col1 if len(cols) == 1 else (col1 if i % 2 == 0 else col2)

        with col:
            st.markdown(f"## {topic.title()}")

            for article in adata[topic][:num]:
                img = article.get('urlToImage', None)
                title = article.get("title", 'No title available')
                url =  article.get('url', None)
                src = article.get('source', {}).get('name', 'Couldn\'t gather source')
                whenpublished = article.get('publishedAt', None)
                dateonly = whenpublished.split('T')[0] if whenpublished else 'Unknown Date'
            
                if img:
                    st.image(img, use_container_width=True)
                else:
                    st.caption("No image available")
                st.markdown(f"##### {title}")
                st.caption(f"Source: {src}")
                if whenpublished:
                    st.caption(f"Dated: {dateonly}", text_alignment = 'right')

                if url: 
                    st.link_button("Read More", url)
                st.write('\n\n')
            
            if len(adata)>2:
                st.divider()

    
def main():
    app_ui()

main()