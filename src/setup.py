from setuptools import setup, find_packages

setup(
    name='Predicting Sales',
    packages=find_packages(),
    version='0.1.0',
    description='using Machine Learning to predict sales given marketing budget',
    include_package_data=True,
    install_requires=[
        'pandas',
        'scikit-learn',
        'joblib',
        'fastapi',
        'uvicorn',
    ],
    entry_points={
        'console_scripts': [
            'sales-predictor-train = sales_prediction.train:main',
        ]
    }
)