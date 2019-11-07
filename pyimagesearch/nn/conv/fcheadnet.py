from keras.layers.core import Dropout, Flatten, Dense


class FCHeadNet:
    @staticmethod
    def build(base_model, classes, units):
        """
        A 2 layers FC network.
        :param base_model: the body of the network
        :param classes: total number of classes
        :param units: the number of nodes in a layer
        :return:
        """
        # initialize the head model that will be placed on
        # top of the base, then add a FC layer
        head_model = base_model.output
        head_model = Flatten(name='flatten')(head_model)
        head_model = Dense(units, activation='relu')(head_model)
        head_model = Dropout(.5)(head_model)

        # add a softmax layer
        head_model = Dense(classes, activation='softmax')(head_model)

        return head_model
