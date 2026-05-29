import random
import time


class ResidualMemory:
    """
    해결되지 않은 기억 조각
    """

    def __init__(self, trigger, context):
        self.trigger = trigger
        self.context = context

        # 기억은 은근히 무겁다
        self.memory_weight = bytearray(1024 * 1024)

        print(f"[TRACE] residual memory attached to '{trigger}'")

    def __del__(self):
        # 정리된 줄 알았는데 사실 남아 있음
        pass


# 머릿속 구석
background_thoughts = []


class KangSiHyeonMind:
    def __init__(self):
        self.expensive_purchases = [
            "CUSTOM TITANIUM KEYBOARD KIT",
            "LIMITED GAME SKIN PACKAGE",
            "INDIE GAME SUPPORTER EDITION",
            "MIDNIGHT AUDIO DAC"
        ]

        self.cheap_foods = [
            "냉동 돈까스",
            "컵라면",
            "삼각김밥",
            "편의점 핫도그"
        ]

        self.emotional_triggers = {
            "돈까스": [
                "형이 살아 있었을 때",
                "싸운 날 저녁",
                "조용한 집",
                "익숙한 냄새",
                "괜히 아끼던 습관"
            ]
        }

    def consume(self, food):
        print(f"[INFO] consuming: {food}")

        if food in self.emotional_triggers:

            print("[INFO] familiar emotional pattern detected")

            fragments = self.emotional_triggers[food]

            trauma_depth = random.randint(1, len(fragments))

            for i in range(trauma_depth):
                background_thoughts.append(
                    ResidualMemory(food, fragments[i])
                )

            print("[WARN] emotional cache could not be cleared")
            print(f"[INFO] lingering thoughts: {len(background_thoughts)}")

            self.reflect(food)

        else:
            print("[INFO] emotional stability maintained")

    def reflect(self, food):
        print()
        print(f"[THINK] why does {food} still feel familiar?")
        time.sleep(0.5)

        purchase = random.choice(self.expensive_purchases)

        print(f"[CARD] 812000 KRW approved")
        print(f"[ITEM] {purchase}")

        time.sleep(0.5)

        print()
        print("[THINK] ...wait")
        print("[THINK] then why did I hesitate over 5490 KRW?")
        print()

        time.sleep(1)

        print(f"[BLAME] '{food}', this is somehow your fault")
        print()

    def status(self):
        size = len(background_thoughts)

        if size > 5:
            print("[SYSTEM] warmth detected")

        if size > 15:
            print("[SYSTEM] memory saturation rising")

        if size > 30:
            print("[CRITICAL] unresolved domestic nostalgia overflow")


def main():
    print("=== ReflectionLeakEngine v0.1 ===")
    print("memory is functioning normally")
    print()

    mind = KangSiHyeonMind()

    while True:
        try:
            food = input("> ")

            mind.consume(food)
            mind.status()

            print()

        except KeyboardInterrupt:
            print()
            print("[INFO] unable to clean residual memories")
            print("[INFO] some warmth still remains")
            break


if __name__ == "__main__":
    main()