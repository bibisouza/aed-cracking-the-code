from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    while root is not None:
        if (
            value1 < root.get_value()
            and value2 < root.get_value()
        ):
            root = root.get_left_child()
        elif (
            value1 > root.get_value()
            and value2 > root.get_value()
        ):
            root = root.get_right_child()
        else:
            return root.get_value()
