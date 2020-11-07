from base import Session, engine, Base
from attack import Attack


def insert_attack(host, port):
    Base.metadata.create_all(engine)
    session = Session()

    attack = Attack(host, port)
    session.add(attack)

    session.commit()
    session.close()


def get_all_attacks():
    session = Session()
    attacks = session.query(Attack).all()

    session.close()
    return attacks


def analyse_attacks():
    print('[i] Analyse all attacks')
    for attack in get_all_attacks():
        tcpdump_analyse(attack)
    print('[i] Analyse completed')


def tcpdump_analyse(attack):
    print('- [i] Anlayse attack id : ', attack.id)
    # tcpdump functions
