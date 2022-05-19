# ZenApp
ZenApp is a **project** in which we had to **identify feelings** from **diary entries**.

## Application
We used **streamlit** in order to quickly build a basic application answering our need.

We also decided not to use an authentification with a password system in order to **keep it simple**. The project was more about the model than the application anyway.

## API and Database
In order to make a **database** and an **API that commmunicates with it**, we used a **docker-compose** managing a **postgresql** and a **FastAPI** part. You can have more informations on [the repository](https://github.com/HumanBojack/ZenAPI).

## Model
We had to try different approaches such as :
- Sklearn + LNTK
- Keras
- FastText + TextHero

For this, we used a [dataset from kaggle](https://www.kaggle.com/datasets/ishantjuyal/emotions-in-text) and another one from [data.world](https://data.world/crowdflower/sentiment-analysis-in-text) in order to try a **data augmentation**.
We ended up using the **Keras** model because it yielded to the best results.
