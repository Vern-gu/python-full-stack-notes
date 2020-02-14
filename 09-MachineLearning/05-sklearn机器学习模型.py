# 估计器（estimator）为所有机器学习算法的父类

"""
import sklearn
1.用于分类的估计器：
    sklearn.neighbor.KNeighborClassifier(n_neighbors=5,algorithm='auto')    k邻近算法
        n_neighbors k值；algorithm选择最合适的计算距离的算法（ball_tree,kd_tree,auto）
    sklearn.naive_bayes.MultinormialNB(alppha=1.0)  朴素贝叶斯算法
        alpha 拉普拉斯平滑系数
    klearn.linear_model.LogisticRegression(solver='liblinear', penalty='l2', C=1.0) 逻辑回归
        solver 优化方法，默认使用了liblinear库实现，内部使用了坐标轴下降算法来迭代优化损失函数
        penalty 正则化种类；C 正则化力度，即惩罚系数λ
    sklearn.tree.DecisionTreeClassifier(criterion='gini', max_depth=None, random_state=None)  决策树与随机森林
        criterion 决策树划分依据，默认为'gini系数'，可以修改为信息熵增益'entropy'
        max_depth 树的深度大小，默认为尽可能拟合所有数据，分得会比较细（但有过拟合风险）
        random_state 随机数种子
    sklearn.tree.export_graphviz(estimator,out_file='tree.dot',feature_names=['','']) 保存树的结构到dot文件(可视化)
    sklearn.ensemble.RandomForestClassifier(n_estimators=10,criterion='gini',max_depth=None,bootstrap=True,random_state=None,min_samples_split=2)
        n_estimator 森林中树的数量；criterion 划分依据；bootstrap 对数据集随机有放回的抽样
        max_features 每个决策树的最大特征数量；min_samples_split 节点划分最少样本数量

2.用于回归的估计器：
    sklearn.linear_model.LinearRegression(fit_intercept=True)   线性回归(使用正规方程进行优化)
        fit_intercept 是否计算偏置
        LinearRegression.coef_ 回归权重
        LinearRegression.intercept_ 偏置
    sklearn.linear_model.SGDRegressor(loss='squared_loss', fit_intercept=True, learning_rate='invscaling', eta0=0.01)  使用随机梯度下降来优化模型
        loss 损失函数类型；fit_intercept 是否计算偏置；learning_rate 学习速率
        SGDRegressor.coef_ 回归权重
        SGDRegressor.intercept_ 偏置
    sklearn.linear_model.Ridge(alpha=1.0, fit_intercept=True, solver='auto', normalize=False)  岭回归(具有L2正则化的线性回归)
        alpha 正则化力度，即惩罚项系数λ，取值0~1，1~10；
        solver 根据数据自动选择优化方法，如果数据量较大，会自动选择sag；normalize 数据是否进行标准化
        Ridge.coef_：回归权重
        Ridge.intercept_：偏置
        # Ridge方法相当于使用了SGDRegressor(penalty='l2')，但仍推荐使用Ridge，因为其实现了SAG随机平均梯度下降，效率更高

3.用于无监督学习的估计器：
    sklearn.cluster.KMeans(n_cluster=8, init='k-means++')  聚类
        n_cluster 开始的聚类中心数量，即K值
        init 初始化方法，默认为‘k-means++’
        labels_ 默认标记的类型，可以和真实值比较

使用方法：
    先实例化一个estimator，
    estimator.fit(x_train,y_train)  计算并生成模型
    estimator.predict(x_test)       进行预测
    estimator.score(x_test,y_test)  评估模型准确率

模型调优： 用于获取最佳的超参数
    sklearn.model_selection.GridsearchCV(estimator, param_grid=None, cv=None)   网格搜索与交叉验证
        param_grid 估计器参数（字典，{"n_neighbors":[1,3,5]}）；cv指定几折交叉验证
    调优后的估计器可以获得几个属性（best_params_, best_score_, best_estimator_, cv_results_）

模型误差评估：
    sklearn.metrics.mean_squared_error(y_true,y_pred)  计算模型的均方误差
        y_true 真实值；y_pred 预测值
        return 浮点数结果
    sklearn.metrics.classification_report(y_true,y_pred,labels=[],target_names=None)  分类评估报告
        labels 指定类别对应的数字：target_names 目标类别名称
        return 每个类别的精确率与召回率
    sklearn.metrics.roc_auc_score(y_true,y_score)  计算roc&auc指标
        y_true 每个样本的真实类别，必须用0(反例)，1(正例)标记
        y_score 预测得分，可以是正类的估计概率、置信值、或分类器方法的返回值
    sklearn.metrics.silhouette_score(X, labels)   计算所有样本的平均轮廓系数
        X 特征值；labels 被聚类标记的目标值

模型的保存和加载：
    from sklearn.externals import joblib
        保存：joblib.dump(rf,'name.pkl')  rf为预估器对象
        加载：estimator = joblib.load(‘name.pkl’)
"""

