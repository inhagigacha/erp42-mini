
from lib.planner_utils.ego import EgoVehicle
from lib.planner_utils.sensor_hub import SensorHub
import rospy
a = 1

class Planner:
    def __init__(self):
        rospy.init_node('planner', anonymous=None)
        self.ego = EgoVehicle()
        self.sensor_hub = SensorHub(ego)    
        self.index_finder = IndexFinder(ego)
        self.mission_planner = MissionPlanner(ego)
        self.path_planner = PathPlanner(ego)

        
    def run(self):

        while True:
            self.index_finder.run()
            self.mission_planner.run()
            self.path_planner.run()
            rospy.Publish()




if __name__ == "__main__":
    pp = Planner()
    pp.run()

        