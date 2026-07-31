import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

from training.config import (
    CONFUSION_MATRIX_PATH,
    CLASSIFICATION_REPORT_PATH,
)

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    recall_score,
    precision_score,
    classification_report,
    confusion_matrix,
)


def plot_consufion_matrix(
        confusion_matrix_df, 
        show_plots, 
        confusion_matrix_path
        ) -> None:


    plt.figure(figsize=(6, 4))
    sns.heatmap(confusion_matrix_df, annot=True, fmt='d', cmap='Blues')

    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    
    Path(confusion_matrix_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(confusion_matrix_path)

    if show_plots:
        plt.show()



def save_classification_report_txt(
        classification_report_txt: str, 
        classification_report_path
        ) ->None:
    
    Path(classification_report_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    
    with open(classification_report_path, 'w') as fp:
        fp.write(classification_report_txt)



def evaluate_model(
        y_test,
        y_pred, 
        show_plots=False, 
        confusion_matrix_path=CONFUSION_MATRIX_PATH, 
        classification_report_path=CLASSIFICATION_REPORT_PATH,
        ) -> dict:

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
    }

    plot_consufion_matrix(
        confusion_matrix_df = CM,
        show_plots = show_plots, 
        confusion_matrix_path= confusion_matrix_path
        )
    save_classification_report_txt(
        classification_report_txt = CR, 
        classification_report_path = classification_report_path
        )

    return metrics_output
    #-----------------------------------------------------
