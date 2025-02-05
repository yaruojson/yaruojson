import os


def process_file(file_path):
    """
    指定ファイルを読み込み、"<hr size=" を含む行およびその以降の行を削除して上書き保存する。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    marker_found = False

    for line in lines:
        if "<hr size=" in line:
            # マーカー行を見つけたので、マーカー行以降は追加せずループを終了
            marker_found = True
            break
        new_lines.append(line)

    if marker_found:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Processed: {file_path}")
    else:
        # マーカーがなかった場合はそのままにする
        print(f"No marker found in: {file_path}")


def process_folder(root_folder):
    """
    指定フォルダ内（サブフォルダも含む）の *.txt ファイルをすべて処理する。
    """
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(".txt"):
                file_path = os.path.join(root, file)
                process_file(file_path)


if __name__ == "__main__":
    # 処理対象のフォルダパスをユーザから入力
    folder_path = input("処理するフォルダのパスを入力してください: ")
    process_folder(folder_path)
