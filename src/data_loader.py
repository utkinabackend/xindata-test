import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        return self.data

    def get_summary(self):
        return self.data.describe()

    def get_crypto_income_diff(self):
        """Сравнивает доходы с криптовалютой и без"""
        crypto_income = self.data[self.data['Payment_Method'] == 'Crypto']['Earnings_USD'].mean()
        non_crypto_income = self.data[self.data['Payment_Method'] != 'Crypto']['Earnings_USD'].mean()
        diff_percent = ((crypto_income - non_crypto_income) / non_crypto_income * 100) if non_crypto_income else 0
        return f"Средний доход с криптовалютой: ${crypto_income:.2f}, без: ${non_crypto_income:.2f}. Разница: {diff_percent:.2f}%."

    def get_region_income_dist(self):
        """Распределение доходов по регионам"""
        region_stats = self.data.groupby('Client_Region')['Earnings_USD'].agg(['mean', 'count']).round(2)
        return region_stats.to_string()

    def get_expert_project_percent(self):
        """Процент экспертов с <100 проектами"""
        experts = self.data[self.data['Experience_Level'] == 'Expert']
        percent = (experts[experts['Job_Completed'] < 100].shape[0] / experts.shape[0] * 100) if experts.shape[0] else 0
        return f"{percent:.2f}% экспертов выполнили менее 100 проектов."

    def get_platform_income(self):
        """Сравнение доходов на Upwork и Fiverr"""
        upwork_income = self.data[self.data['Platform'] == 'Upwork']['Earnings_USD'].mean()
        fiverr_income = self.data[self.data['Platform'] == 'Fiverr']['Earnings_USD'].mean()
        return f"Средний доход на Upwork: ${upwork_income:.2f}, на Fiverr: ${fiverr_income:.2f}."

    def get_category_project_dist(self):
        """Распределение проектов по категориям"""
        category_stats = self.data.groupby('Job_Category')['Job_Completed'].agg(['sum', 'count']).round(2)
        return category_stats.to_string()
