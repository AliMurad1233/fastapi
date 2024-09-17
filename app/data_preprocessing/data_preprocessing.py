import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def preprocess_data(df: pd.DataFrame):
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Fare'].fillna(df['Fare'].mean(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    X = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
    y = df['Survived']

    # Preprocessing: One-hot encode categorical variables
    numeric_features = ['Age', 'Fare']
    categorical_features = ['Pclass', 'Sex', 'Embarked']

    # Create preprocessing pipeline
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())])

    categorical_transformer = Pipeline(steps=[
        ('encoder', OneHotEncoder())])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    X_preprocessed = preprocessor.fit_transform(X)

    return X_preprocessed, y
