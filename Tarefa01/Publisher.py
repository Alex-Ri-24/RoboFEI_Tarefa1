import rclpy
from rclpy.node import Node

from std_msgs.msg import String

# Superclasse = Node
# Subclasse   = Publisher
class Publisher(Node):
    
    # Método que vai construir o nó ""publisher"
    def __init__(self):
        super().__init__('Publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5              # tempo de publicação da mensagem (s)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0                      # contador para callbac

    # Método que publica a mensagem
    def timer_callback(self):
        msg = String()
        msg.data = 'Teste %d' % self.i  # O que está sendo publicado no terminal
        self.publisher_.publish(msg)
        self.get_logger().info('Publicando: "%s"' % msg.data)
        self.i += 1

# Função principal
def main(args=None):
    rclpy.init(args=args)

    # Uma variável do tipo Publisher()
    nodePublisher = Publisher()

    # Executa uma iteração do loop de processamento de mensagens
    rclpy.spin(nodePublisher)

    # Destrói o nó criado
    nodePublisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()