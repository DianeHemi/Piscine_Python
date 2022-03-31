class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            raise Exception("Error : Lists are of a different length")
        result = 0.0
        for w, c in zip(words, coefs):
            result += len(w) * c
        return result

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            raise Exception("Error : Lists are of a different length")
        result = 0.0
        for i, (w, c) in enumerate(zip(words, coefs)):
            result += len(w) * c
        return result
        