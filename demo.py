from dup_fmt.formatter import Datetime, FormatterGroupRevision, Naming

if __name__ == "__main__":

    class DatetimeNaming(FormatterGroupRevision):
        base_groups = {
            "timestamp": Datetime,
            "naming": Naming,
        }

    dn: FormatterGroupRevision = DatetimeNaming.parse(
        "2021_01_01_data_engineer_05_05_29_data engineer",
        fmt="{timestamp:%Y_%m_%d}_{naming:%s}_{timestamp:%H_%M_%S}_{naming}",
    )

    print(dn)
    print(dn.format(fmt="{timestamp:%Y}"))
