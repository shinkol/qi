########################################################
#                       STEPS                          #
########################################################
"""
1) API LISTENER
2) UPLOAD FILES
3) READ FILES
4) CLASSIFY IPV
5) REFORMAT THE IPV
6) FORWARD THE IP'S TO THE MASSAGE QUEUE
"""
########################################################
from api import Api


def main():
    api = Api()
    api.run()

if __name__ == "__main__":
    main()