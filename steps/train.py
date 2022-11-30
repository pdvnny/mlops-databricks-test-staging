"""
This module defines the `train` routine for our financial fraud detection model

- The returned object is a trained CrossValidator Spark model

- ``estimator_fn``: Defines the customizable estimator type and parameters that are used
  during training to produce a model recipe.

"""

from typing import Dict, Any


def estimator_fn(estimator_params: Dict[str, Any] = None) -> Any:
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    
    """
    from sklearn.tree import DecisionTreeClassifier
    
    # Optimial parameters based on previous work
    max_bins = 10
    max_depth = 5
    model = DecisionTreeClassifier(max_depth=max_depth, max_leaf_nodes=max_bins)
    
    return model


"""
    ** This approach did not work ... I'll have to changes things up later **
    
    
    # The estimator will be a PySpark `DecisionTreeClassifier`
    

    from pyspark.ml.classification import DecisionTreeClassifier
    from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
    from pyspark.ml.evaluation import BinaryClassificationEvaluator
    
    evaluatorAUC = BinaryClassificationEvaluator(labelCol = 'label', rawPredcitionCol = 'prediction', metricName = 'areaUnderROC')
    
    dt = DecisionTreeClassifier(**estimator_params)  # TO DO: double check that this setup works
    
    paramGrid = (
        ParamGridBuilder()
            .addGrid(dt.maxDepth, [5, 10, 15])
            .addGrid(dt.maxBins, [10, 20, 30])
            .build()
    )
    
    cv = CrossValidator(
        estimator = dt,
        estimatorParamMaps = paramGrid,
        evaluator = evaluatorPR,
        numFolds = 3
    )
"""