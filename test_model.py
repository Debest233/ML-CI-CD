import numpy as np
from model import train_and_predict, get_accuracy

def test_predictions_not_none():
    """Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję."""
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."

def test_predictions_length():
    """Test 2: Sprawdza, czy długość listy predykcji jest > 0 i odpowiada próbkom testowym."""
    preds, y_test = train_and_predict()
    assert len(preds) > 0, "Długość predykcji powinna być większa od zera."
    assert len(preds) == len(y_test), "Liczba predykcji musi odpowiadać liczbie testowych etykiet."

def test_predictions_value_range():
    """Test 3: Sprawdza, czy wartości mieszczą się w zakresie dla zbioru Iris (0, 1, 2)."""
    preds, _ = train_and_predict()
    # Sprawdzamy, czy każda przewidziana klasa znajduje się w dopuszczalnym zbiorze
    assert all(p in [0, 1, 2] for p in preds), "Predykcje zawierają nieoczekiwane klasy!"

def test_model_accuracy():
    """Test 4 (na 5): Sprawdza, czy model osiąga co najmniej 70% dokładności."""
    accuracy = get_accuracy()
    assert accuracy >= 0.70, f"Dokładność modelu jest zbyt niska i wynosi {accuracy}"