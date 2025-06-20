from data_loader import DataLoader
from llm_processor import LLMProcessor


def main():
    data_path = "../data/freelancer_earnings_bd.csv"
    loader = DataLoader(data_path)
    processor = LLMProcessor()

    query_handlers = {
        ("криптовалют", "доход"): loader.get_crypto_income_diff,
        ("регион",): loader.get_region_income_dist,
        ("эксперт", "проект"): loader.get_expert_project_percent,
        ("платформ", "upwork", "fiverr"): loader.get_platform_income,
        ("категори", "проект"): loader.get_category_project_dist,
    }

    try:
        loader.load_data()
        print("Данные загружены.")

        while True:
            query = input("Введите запрос (или 'выход' для завершения): ")
            if query.lower() == 'выход':
                break

            query_lower = query.lower()
            context = "Неизвестный запрос. Попробуйте слова: криптовалюта, регионы, эксперты, платформы, рейтинг, категории."
            for keywords, handler in query_handlers.items():
                if all(keyword in query_lower for keyword in keywords):
                    context = handler()
                    break

            response = processor.process_query(query, context)
            print(f"Ответ: {response}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    main()
