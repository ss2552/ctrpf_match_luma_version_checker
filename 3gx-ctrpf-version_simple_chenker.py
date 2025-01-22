err:None = lambda msg:exit(print(msg,"\n"))

def get_version(fp: str) -> tuple:
    try:
        # if not fp.endswith(p:=".3gx"): fp+=p
        with open(fp, "rb") as f:
            from struct import unpack
            magic_number, revision, minor, major = unpack('8sxBBB', f.read(12))
            if magic_number == b"3GX$0001":
                return major, minor, revision
            err("3gxではありません")
    except FileNotFoundError:
        err("ファイルが見つかりません")
    except Exception as e:
        err(e)

def ctrpf_version_to_loader_version(major:int, minor:int) -> tuple:
    try:
        return [
            {
                8: (
                    (1,0,2), [0]
                ),
                7: (
                    (1,0,1), [4,3,2,1]
                ),
                6: (
                    (1,0,0), [0]
                ),
                5: (
                    (0,0,0), [1]
                )
            }
        ][major][minor]
    except Exception as e:
        err(e)

def search_firm_and_version(version: tuple) -> tuple:
    try:
        auther_repo_name: dict = [
            ("PabloMK7", ["Luma3DS_3GX"]),
            ("LumaTeam", ["Luma3DS"])
        ]
        version_list: list = [
            [
                [
                    [
                        (0, 0, [(9,1)])
                    ]
                ]
            ],
            [
                [
                    [
                        (0, 0, [(10,2,1),(10,3),(11,0),(12,0)])
                    ],
                    [
                        (0, 0, [(13,0),(13,0,1),(13,0,2),(13,1)])
                    ],
                    [
                        (1, 0, [(13,1,1),(13,1,2),(13,2),(13,2,1),(13,3)])
                    ]
                ]
            ]
        ]
        a,b,c=version
        r:list = []
        for d in version_list[a][b][c]:
            auther, repo, vers = d
            auther_name, repository_names = auther_repo_name[auther]
            repository_name:int = repository_names[repo]
            r.append((auther_name, repository_name, vers))
        return r
    except Exception as e:
        err(e)

if __name__ == "__main__":
    bar32 = "-"*32;bar64="-"*64;print(bar32)
    
    keys = ["はい", "は", "yes", "y", "ゆうま村長"]
    key=input("githubリンクにしますか？\n\t（"+("/".join(keys))+"）\n");print(bar32)

    ctrpf_file_name: str = input(" - ファイル名.3gx -\n");print(bar32+"\n\n"+bar32)

    ctrpf_major_version, ctrpf_minor_version, ctrpf_revision_version = get_version(ctrpf_file_name)
    print(f"ctrpf バージョン:\t{ctrpf_major_version}.{ctrpf_minor_version}.{ctrpf_revision_version}"+"\n"+bar32)

    loader_version, ctrpf_revision = ctrpf_version_to_loader_version(ctrpf_major_version, ctrpf_minor_version)
    a,b,c=loader_version;print(f"loader バージョン\t{a}.{b}.{c}\n"+bar32+("\n\n"));del a,b,c

    github_link: bool = 1 if key in keys else 0

    info: tuple = search_firm_and_version(loader_version)
    for auther_name, repository_name, versions in info:
        print("\n"+"~"*64)

        print("名前:\t\t"+auther_name+"\n"+bar64)

        print("リポジトリ名:\t"+repository_name+"\n"+bar64)

        print(" - バージョン -")
        for version in versions:
            vs:list = [str(v) for v in version]
            v: str = ".".join(vs)
            print(" *",v)

            if github_link:
                print(f"  - https://github.com/{auther_name}/{repository_name}/releases/tag/v{v}")

        print(bar64)

    
    if key == keys[4]:print("\n\n\n\t --- https://www.youtube.com/@yumasonchou ---\n\n")
    print("\n" if ctrpf_revision_version in ctrpf_revision else f"\n* revision バージョンが不明でした\n* 動かない可能性があります\n")
