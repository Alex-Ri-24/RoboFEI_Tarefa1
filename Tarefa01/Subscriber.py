import rclpy
from rclpy.node import Node

from std_msgs.msg import String

# Superclasse = Node
# Subclasse   = Subscriber
class Subscriber(Node):
    
    # Método que vai construir o nó "subscriber"
    def __init__(self):
        super().__init__('Subscriber')
        self.subscription = self.create_subscription(String,'topic', self.listener_callback, 10)

    # Método que lê a mensagem
    def listener_callback(self, msg):
        self.get_logger().info('Recebo: "%s"' % msg.data)

# Função principal
def main(args=None):
    rclpy.init(args=args)

    nodeSubscriber = Subscriber()

    # Executa uma iteração do loop de processamento de mensagens
    rclpy.spin(nodeSubscriber)

     # Destrói o nó criado
    nodeSubscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()