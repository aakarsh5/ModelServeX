# train.py
import argparse
import tensorflow as tf

layers = tf.keras.layers
models = tf.keras.models

def build_model(input_shape=(32, 32, 3), num_classes=10):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.BatchNormalization(),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),

        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),

        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

def main(epochs=10, batch_size=64, output='model.h5'):
    # Load CIFAR-10 dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    x_train = x_train.astype('float32') / 255.0
    x_test  = x_test.astype('float32') / 255.0

    # Build & compile model
    model = build_model()
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.summary()

    # Train model
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1)

    # Evaluate
    loss, acc = model.evaluate(x_test, y_test, verbose=2)
    print(f"Test accuracy: {acc:.4f}")

    # Save model
    model.save(output, include_optimizer=False)
    print(f"✅ Model saved to {output}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--output', type=str, default='model.h5')
    args = parser.parse_args()
    main(args.epochs, args.batch_size, args.output)
