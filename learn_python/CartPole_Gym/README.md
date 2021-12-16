# CartPole_Gym


*Solving CartPole from Gym (from OpenAI) using CrossEntropy method*

After about 250 iterations and still training:

![ezgif com-gif-maker](https://user-images.githubusercontent.com/57571014/93023937-d3a63f80-f5f2-11ea-8f18-dc17c4d9f78b.gif)

### Modules (third-parties):
- Pytorch
- Gym (CartPole)
- Numpy
- Matplotlib

## About
In CrossEntropy method (naive) you take certain percentile (70) and based on it you let survive (observation, actions) by rewards survive and other data you erase and you train agent (Here it is Net). You take observations from environment and pass them to agent (Neural Network -> Net) to get action (Here it is probability of action and than randomly choose between them (for early exploration, later NN will be trained for randomness)). You use selected action (In the CartPole it is only 0 or 1 (left and right)) to perform action in environment and you extract (next_observation, reward, is_done, {}), where next_observation is predictment; reward is later used for determining that percentile and if program can earn near 200 (maximum) reward; is_done is one round of the CartPole (boolean). Later this already processed data are used for training agent (Net).

You can also render the CartPole: In "iterate_batches(env, net, BATCH_SIZE, render=False)" you need set render to True. And of course you can play with tweaking program.

Also here are results of my training:
![Figure_1](https://user-images.githubusercontent.com/57571014/93024209-005b5680-f5f5-11ea-8cd0-ba70e129b1ab.png)
![Figure_2](https://user-images.githubusercontent.com/57571014/93024210-02251a00-f5f5-11ea-9eb4-05459ac031a0.png)
