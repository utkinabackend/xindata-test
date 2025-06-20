from data_loader import DataLoader
from llm_processor import LLMProcessor


def main():
    data_path = "../data/freelancer_earnings_bd.csv"
    loader = DataLoader(data_path)
    processor = LLMProcessor()

    try:
        data = loader.load_data()
        print("Данные загружены:")
        print(loader.get_summary())

        data_context = "Средний доход: $5000. 10% используют криптовалюту, доход выше на 20%."
        query = "Что ты можешь сказать исходя из этих данных?"
        response = processor.process_query(query, data_context)
        print(f"Ответ: {response}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()
