
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score,
    precision_score,
    classification_report,
    confusion_matrix,
)

def plot_consufion_matrix(cm_df):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    # 4. Plot using seaborn
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues')

    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')

    plt.show()



def evaluate_model(y_test, y_pred) -> dict:
   # Calculate metrics
    #--------------------------------------------------
    accuracy = accuracy_score(
        y_true = y_test,
        y_pred = y_pred,
    )

    precision = precision_score(
        y_true = y_test,
        y_pred = y_pred,
        average="macro",
    )

    recall = recall_score(
        y_true = y_test,
        y_pred = y_pred,
        average="macro",
    )

    f1 = f1_score(
        y_true = y_test,
        y_pred = y_pred,
        average="macro",
    )

    CM = confusion_matrix(
        y_true= y_test,
        y_pred= y_pred,
    )

    CR = classification_report(
        y_true = y_test,
        y_pred = y_pred,
    )

    metrics_output = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion matrix": CM,
        "clasiffication report": CR,
    }

    plot_consufion_matrix(CM)

    return metrics_output
    #-----------------------------------------------------
