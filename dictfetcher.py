from fnmatch import fnmatch


class DictFetcherMixin(object):
    def get_doc_by_path(self, path):
        if type(path) == str:
            path = path.split(".")

        length = len(path)

        def dfs(doc, path, index, cur_path, r):
            # print path, index, cur_path, r
            if index >= length:
                r[".".join(cur_path)] = doc
                return 
            arg = path[index]
            for key in doc:
                if fnmatch(key, arg):
                    # print key
                    dfs(doc[key], path, index+1, cur_path+[key], r)

                if arg in doc:
                    dfs(doc[arg], path, index+1, cur_path+[arg], r)

        r = {}
        dfs(self, path, 0, [], r)
        return r

    def __missing__(self, path):
        return self.get_doc_by_path(path)











