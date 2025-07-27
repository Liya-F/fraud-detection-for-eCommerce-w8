from sklearn.metrics import (
    f1_score,
    classification_report,
    confusion_matrix,
    precision_recall_curve,
    auc,
    roc_curve,
    RocCurveDisplay,
    PrecisionRecallDisplay
)
import matplotlib.pyplot as plt
import seaborn as sns

class ModelEvaluator:
    def __init__(self, model_name="Model"):
        self.model_name = model_name

    def evaluate(self, y_true, y_pred, y_proba=None, show_plots=True):
        print(f"\n🧪 Evaluation Report for {self.model_name}")
        print("-" * 40)
        print("F1 Score:", f1_score(y_true, y_pred))
        print("\nClassification Report:\n", classification_report(y_true, y_pred))
        
        # Confusion Matrix
        cm = confusion_matrix(y_true, y_pred)
        if show_plots:
            plt.figure(figsize=(5, 4))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title(f'Confusion Matrix - {self.model_name}')
            plt.xlabel('Predicted')
            plt.ylabel('Actual')
            plt.show()

        # Precision-Recall AUC
        if y_proba is not None:
            precision, recall, _ = precision_recall_curve(y_true, y_proba)
            pr_auc = auc(recall, precision)
            print("Precision-Recall AUC:", pr_auc)

            if show_plots:
                PrecisionRecallDisplay(precision=precision, recall=recall).plot()
                plt.title(f'Precision-Recall Curve - {self.model_name}')
                plt.show()

                fpr, tpr, _ = roc_curve(y_true, y_proba)
                RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
                plt.title(f'ROC Curve - {self.model_name}')
                plt.show()
