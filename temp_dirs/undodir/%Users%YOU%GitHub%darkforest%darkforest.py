Vim�UnDo� �AdO��y����A��"�t�qт   m   print map(np.mean, reward_mat)   i         @       @   @   @    Z��   ) _�                            ����                                                                                                                                                                                                                                                                                                                                                             Zd��    �         h      import gym_darkforest5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       Zd��    �         h      $import gym-darkforest.gym_darkforest5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Zd�W    �         i       �         h    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Zd�h    �                
import gym5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Zd��    �         h      import gym_darkforest5�_�                    Q       ����                                                                                                                                                                                                                                                                                                                            c           Q          V       Zd��    �   b   d          )�   a   c          .    ar=np.mean(runner.episode_rewards[-100:]))�   `   b              ep=runner.episode,�   _   a          cprint("Learning finished. Total episodes: {ep}. Average reward of last 100 episodes: {ar}.".format(�   ^   `          # Print statistics�   ]   _           �   \   ^          Vrunner.run(episodes=100, max_episode_timesteps=200, episode_finished=episode_finished)�   [   ]          # Start learning�   Z   \           �   Y   [           �   X   Z              return True�   W   Y          o                                                                                 reward=r.episode_rewards[-1]))�   V   X          u    print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,�   U   W          def episode_finished(r):�   T   V          /# Callback function printing episode statistics�   S   U           �   R   T           �   Q   S          -runner = Runner(agent=agent, environment=env)�   P   R          # Create the runner5�_�      	              Q       ����                                                                                                                                                                                                                                                                                                                            c          Q          V       Zdؿ   	 �   b   d          # )�   a   c          0#     ar=np.mean(runner.episode_rewards[-100:]))�   `   b          #     ep=runner.episode,�   _   a          e# print("Learning finished. Total episodes: {ep}. Average reward of last 100 episodes: {ar}.".format(�   ^   `          # # Print statistics�   ]   _           �   \   ^          X# runner.run(episodes=100, max_episode_timesteps=200, episode_finished=episode_finished)�   [   ]          # # Start learning�   Z   \           �   Y   [           �   X   Z          #     return True�   W   Y          q#                                                                                  reward=r.episode_rewards[-1]))�   V   X          w#     print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,�   U   W          # def episode_finished(r):�   T   V          1# # Callback function printing episode statistics�   S   U           �   R   T           �   Q   S          /# runner = Runner(agent=agent, environment=env)�   P   R          # # Create the runner5�_�                	           ����                                                                                                                                                                                                                                                                                                                                                             Zd��     �         i       �         h    5�_�   	      
                 ����                                                                                                                                                                                                                                                                                                                                                             Zd��   
 �         i      #assert whatever  # silence pyflakes5�_�                    X        ����                                                                                                                                                                                                                                                                                                                            X   '       Y   '       V   '    Ze�    �   X   Z          o                                                                                 reward=r.episode_rewards[-1]))�   W   Y          u    print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,5�_�                    X       ����                                                                                                                                                                                                                                                                                                                            Y          X          V       Ze�    �   X   Z          q    #                                                                              reward=r.episode_rewards[-1]))�   W   Y          w    # print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,5�_�                    X        ����                                                                                                                                                                                                                                                                                                                            X          Y          V       Ze    �   X   Z          o                                                                                 reward=r.episode_rewards[-1]))�   W   Y          u    print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,5�_�                   `        ����                                                                                                                                                                                                                                                                                                                            d           `           V        Ze     �   c   e          )�   b   d          .    ar=np.mean(runner.episode_rewards[-100:]))�   a   c              ep=runner.episode,�   `   b          cprint("Learning finished. Total episodes: {ep}. Average reward of last 100 episodes: {ar}.".format(�   _   a          # Print statistics5�_�                    e        ����                                                                                                                                                                                                                                                                                                                            d           `           V        Ze     �   e   h   j       �   e   g   i    5�_�                    g       ����                                                                                                                                                                                                                                                                                                                            d           `           V        Ze!     �   f   i   k      for t = 1:105�_�                    g       ����                                                                                                                                                                                                                                                                                                                            g          g          v       Ze)     �   f   h   l      for t = 1:10:5�_�                    g       ����                                                                                                                                                                                                                                                                                                                            g          g          v       Ze*     �   f   h   l      for t 5�_�                    g        ����                                                                                                                                                                                                                                                                                                                            g          g          v       Ze8     �   f   g          for t in range(10) 5�_�                    g        ����                                                                                                                                                                                                                                                                                                                            g          g          v       Ze<     �   f   h   k       5�_�                    g       ����                                                                                                                                                                                                                                                                                                                            g          g          v       ZeD    �   f   h   k      reward_mat = np.array()5�_�                    g   4    ����                                                                                                                                                                                                                                                                                                                            g          g          v       Ze`     �   f   h   k      4reward_mat = np.array(runner.episode_rewards[-100:])5�_�                    g   B    ����                                                                                                                                                                                                                                                                                                                            g          g          v       Zef     �   g   i   l       �   g   i   k    5�_�                    h       ����                                                                                                                                                                                                                                                                                                                            g          g          v       Zew    �   g   i   l      map(sum,reward_mat)5�_�                    h        ����                                                                                                                                                                                                                                                                                                                            g          g          v       Zez    �   g   i   l      map(sum, reward_mat)5�_�                    h   
    ����                                                                                                                                                                                                                                                                                                                            g          g          v       Ze     �   g   i   l      print map(sum, reward_mat)5�_�                    h       ����                                                                                                                                                                                                                                                                                                                            g          g          v       Ze�    �   g   i   l      #print map(lambda x:sum, reward_mat)5�_�                    T        ����                                                                                                                                                                                                                                                                                                                                                             Ze    �   T   V   m       �   T   V   l    5�_�                     _       ����                                                                                                                                                                                                                                                                                                                                                             Ze    �   ^   `   m      Vrunner.run(episodes=100, max_episode_timesteps=200, episode_finished=episode_finished)5�_�      !               h   .    ����                                                                                                                                                                                                                                                                                                                            h   .       h   0       v   0    ZeB     �   g   i   m      Creward_mat = np.array(runner.episode_rewards[-100:]).reshape(10,10)5�_�       "           !   h   .    ����                                                                                                                                                                                                                                                                                                                            h   .       h   0       v   0    ZeD    �   g   i   m      @reward_mat = np.array(runner.episode_rewards[-:]).reshape(10,10)5�_�   !   #           "   h   E    ����                                                                                                                                                                                                                                                                                                                            h   .       h   0       v   0    ZeS    �   g   i   m      Kreward_mat = np.array(runner.episode_rewards[-episode_num:]).reshape(10,10)5�_�   "   $           #   i   
    ����                                                                                                                                                                                                                                                                                                                            i          i   
       v   
    Zej     �   h   j   m      )print map(lambda x:sum(x)/10, reward_mat)5�_�   #   %           $   i   
    ����                                                                                                                                                                                                                                                                                                                            i          i   
       v   
    Zek    �   h   j   m      print map(, reward_mat)5�_�   $   &           %   h   S    ����                                                                                                                                                                                                                                                                                                                                                             Ze	x     �   g   i   m      Wreward_mat = np.array(runner.episode_rewards[-episode_num:]).reshape(episode_num/10,10)5�_�   %   '           &   h   W    ����                                                                                                                                                                                                                                                                                                                                                             Ze	{    �   g   i   m      Xreward_mat = np.array(runner.episode_rewards[-episode_num:]).reshape(episode_num/100,10)5�_�   &   (           '   h        ����                                                                                                                                                                                                                                                                                                                            i           h           V        Ze	�     �   h   j          print map(np.mean, reward_mat)�   g   i          Yreward_mat = np.array(runner.episode_rewards[-episode_num:]).reshape(episode_num/100,100)5�_�   '   )           (   a        ����                                                                                                                                                                                                                                                                                                                            e           a           V        Ze	�    �   d   f          # )�   c   e          0#     ar=np.mean(runner.episode_rewards[-100:]))�   b   d          #     ep=runner.episode,�   a   c          e# print("Learning finished. Total episodes: {ep}. Average reward of last 100 episodes: {ar}.".format(�   `   b          # # Print statistics5�_�   (   *           )   d   '    ����                                                                                                                                                                                                                                                                                                                            e           a           V        Ze
    �   c   e   m      .    ar=np.mean(runner.episode_rewards[-100:]))5�_�   )   +           *   Y       ����                                                                                                                                                                                                                                                                                                                            Z          Y          V       Ze
    �   Y   [          q    #                                                                              reward=r.episode_rewards[-1]))�   X   Z          w    # print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,5�_�   *   ,           +   U       ����                                                                                                                                                                                                                                                                                                                            Z          Y          V       Ze
b     �   T   V   m      episode_num = 5005�_�   +   -           ,   U       ����                                                                                                                                                                                                                                                                                                                            Z          Y          V       Ze
c    �   T   V   m      episode_num = 005�_�   ,   .           -   U       ����                                                                                                                                                                                                                                                                                                                            Z          Y          V       Ze
�    �   T   V   m      episode_num = 10005�_�   -   /           .   U       ����                                                                                                                                                                                                                                                                                                                                                             ZhX�     �   T   V   m      episode_num = 1005�_�   .   0           /   Y        ����                                                                                                                                                                                                                                                                                                                            Y           Y           V        ZhY     �   X   Z          u    print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,5�_�   /   1           0   Y        ����                                                                                                                                                                                                                                                                                                                            Y           Y           V        ZhY     �   X   Z          w    # print("Finished episode {ep} after {ts} timesteps (reward: {reward})".format(ep=r.episode, ts=r.episode_timestep,5�_�   0   2           1   a        ����                                                                                                                                                                                                                                                                                                                            a           f           V        ZhY"     �   e   g           �   d   f          )�   c   e          6    ar=np.mean(runner.episode_rewards[-episode_num:]))�   b   d              ep=runner.episode,�   a   c          cprint("Learning finished. Total episodes: {ep}. Average reward of last 100 episodes: {ar}.".format(�   `   b          # Print statistics5�_�   1   3           2   h        ����                                                                                                                                                                                                                                                                                                                            h           i           V        ZhY%   ! �   h   j           # print map(np.mean, reward_mat)�   g   i          [# reward_mat = np.array(runner.episode_rewards[-episode_num:]).reshape(episode_num/100,100)5�_�   2   4           3   U       ����                                                                                                                                                                                                                                                                                                                                                             ZhY�   " �   T   V   m      episode_num = 10005�_�   3   5           4   -        ����                                                                                                                                                                                                                                                                                                                                                             Zh\    # �   -   /   m    �   -   .   m    5�_�   4   6           5   -   2    ����                                                                                                                                                                                                                                                                                                                                                             Zh\+   $ �   ,   .   n      2    dict(type='dense', size=32, activation='tanh')5�_�   5   7           6   -       ����                                                                                                                                                                                                                                                                                                                                                             Zh^�   % �   ,   -          3    dict(type='dense', size=32, activation='tanh'),5�_�   6   8           7   ,       ����                                                                                                                                                                                                                                                                                                                                                             Zh^�     �   +   -   m      3    dict(type='dense', size=32, activation='tanh'),5�_�   7   9           8   ,       ����                                                                                                                                                                                                                                                                                                                                                             Zh^�   & �   +   -   m      3    dict(type='dense', size=62, activation='tanh'),5�_�   8   :           9   ,       ����                                                                                                                                                                                                                                                                                                                                                             Zha�     �   +   -   m      3    dict(type='dense', size=64, activation='tanh'),5�_�   9   ;           :   ,       ����                                                                                                                                                                                                                                                                                                                                                             Zha�   ' �   +   -   m      3    dict(type='dense', size=34, activation='tanh'),5�_�   :   <           ;   U       ����                                                                                                                                                                                                                                                                                                                                                             Zh�     �   T   V   m      episode_num = 50005�_�   ;   =           <   U       ����                                                                                                                                                                                                                                                                                                                                                             Zh�     �   T   V   m      episode_num = x0005�_�   <   >           =   U       ����                                                                                                                                                                                                                                                                                                                                                             Zh�   ( �   T   V   m      episode_num = 00005�_�   =   ?           >   i       ����                                                                                                                                                                                                                                                                                                                                                             Z��     �   h   j   m      print map(np.mean, reward_mat)5�_�   >   @           ?   i       ����                                                                                                                                                                                                                                                                                                                                                             Z��     �   h   j   m      print( map(np.mean, reward_mat)5�_�   ?               @   i       ����                                                                                                                                                                                                                                                                                                                                                             Z��   ) �   h   j   m      print(map(np.mean, reward_mat)5�_�                    d        ����                                                                                                                                                                                                                                                                                                                            d           d           V        Ze     �   c   e   i       5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             Zd��     �         i      assert whatever  # silence 5�_�              	              ����                                                                                                                                                                                                                                                                                                                                                             Zd��     �         h       �         i      (assert whatever  # silence pyflakesbbbbb5��