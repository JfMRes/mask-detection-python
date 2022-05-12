from imageai.Prediction.Custom import CustomImagePrediction

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
modelo="imagenes\models\model_ex-049_acc-0.906250.h5"
prediction.setModelPath(modelo)
prediction.setJsonPath("imagenes\json\model_class.json")
prediction.loadModel(num_objects=2)
def inicia():
    foto=r"ruta"

    predictions, probabilities = prediction.predictImage(foto, result_count=2)

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction , " : " , eachProbability)
inicia()
