from dup_fmt.formatter import (
    Datetime,
    FormatterGroup,
    FormatterGroupType,
    Group,
    Naming,
)


def demo_fmt():
    nm = Naming.passer(value=["data", "engineer"])
    print(nm)


def demo_fmt_group():
    DatetimeNaming: FormatterGroupType = Group(
        {
            "timestamp": Datetime,
            "naming": Naming,
        }
    )
    dn: FormatterGroup = DatetimeNaming.parse(
        "2021_01_01_data_engineer_05_05_29_data engineer",
        fmt="{timestamp:%Y_%m_%d}_{naming:%s}_{timestamp:%H_%M_%S}_{naming}",
    )

    print(dn)
    print(dn.format(fmt="{timestamp:%Y}_{naming:%c}"))


if __name__ == "__main__":
    # demo_fmt_group()
    demo_fmt()
