def get_version(fp: str) -> tuple:
    try:
        # if not fp.endswith(p:=".3gx"): fp+=p
        with open(fp, "rb") as f:
            from struct import unpack
            revision, minor, major = unpack('bbb', f.read())
            return major, minor, revision
    except Exception as e:
        raise Exception(e)

def ctrpf_version_to_loader_version(major:int, minor:int, revision:int) -> tuple:
    try:
        loader_version, ctrpf_revision = [
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
        
        if revision in ctrpf_revision:
            return loader_version
        else:
            raise Exception(revision)
    except Exception as e:
        raise Exception(e)
    
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
                        (0, 0, [9,1])
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
        raise Exception(e)
    
if __name__ == "__main__":

    print("-"*32)

    keys = ["はい", "は", "yes", "y", "ゆうま村長"]
    key=input("githubリンクにしますか？\t"+("/".join(keys))+"\n")

    print("-"*32)

    ctrpf_file_name: str = input(" - ファイル名.3gx -\n");print("-"*32)
    
    print("ファイル名 || ディレクトリ名:", ctrpf_file_name);print("-"*32)

    print("\n");print("-"*32)

    ctrpf_major_version, ctrpf_minor_version, ctrpf_revision_version = get_version(ctrpf_file_name)
    print(f"ctrpf バージョン:\t{ctrpf_major_version}.{ctrpf_minor_version}.{ctrpf_revision_version}");print("-"*32)
    
    loader_version: tuple = ctrpf_version_to_loader_version(ctrpf_major_version, ctrpf_minor_version, ctrpf_revision_version)
    a,b,c=loader_version;print(f"loader バージョン\t{a}.{b}.{c}");del a,b,c;print("-"*32)
    
    print("\n");print("-"*32)
    
    info: tuple = search_firm_and_version(loader_version)
    for auther_name, repository_name, versions in info:
    
        print("名前:\t\t", auther_name);print("-"*32)
    
        print("リポジトリ名:\t", repository_name);print("-"*32)

        print(" - バージョン -")
        for version in versions:
            vs:list = []
            for v in version:
                vs.append(str(v))
            v: str= ".".join(vs)
            print(" *",v)
                    
            if key in keys:
                print(f"  - https://github.com/{auther_name}/{repository_name}/releases/tag/v{v}")

        print("-"*32)
    
    if key == keys[4]:
        print("\n\t --- https://www.youtube.com/@yumasonchou ---\n")
        