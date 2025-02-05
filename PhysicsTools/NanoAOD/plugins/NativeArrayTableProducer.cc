#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "DataFormats/NanoAOD/interface/FlatTable.h"

#include <vector>

template <typename TIn, typename TCol>
class NativeArrayTableProducer : public edm::stream::EDProducer<> {
public:
  NativeArrayTableProducer(edm::ParameterSet const& params)
      : name_(params.getParameter<std::string>("name")),
        doc_(params.existsAs<std::string>("doc") ? params.getParameter<std::string>("doc") : ""),
        src_(consumes<TIn>(params.getParameter<edm::InputTag>("src"))) {
    produces<nanoaod::FlatTable>();
  }

  ~NativeArrayTableProducer() override {}

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    edm::ParameterSetDescription desc;
    desc.add<std::string>("name")->setComment("name of the branch in the flat table output");
    desc.addOptional<std::string>("doc")->setComment("few words description of the branch content");
    desc.add<edm::InputTag>("src")->setComment("input collection for the branch");

    descriptions.addWithDefaultLabel(desc);
  }

  void produce(edm::Event& iEvent, const edm::EventSetup& iSetup) override {
    const auto& in = iEvent.get(src_);
    auto out = std::make_unique<nanoaod::FlatTable>(in.size(), name_, false, false);
    out->setDoc(doc_);
    (*out).template addColumn<TCol>(this->name_, in, this->doc_);
    iEvent.put(std::move(out));
  }

protected:
  const std::string name_;
  const std::string doc_;
  const edm::EDGetTokenT<TIn> src_;
};

typedef NativeArrayTableProducer<std::vector<float>, float> FloatArrayTableProducer;
typedef NativeArrayTableProducer<std::vector<double>, float> DoubleArrayTableProducer;
typedef NativeArrayTableProducer<std::vector<int>, int> IntArrayTableProducer;
typedef NativeArrayTableProducer<std::vector<bool>, bool> BoolArrayTableProducer;

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(FloatArrayTableProducer);
DEFINE_FWK_MODULE(DoubleArrayTableProducer);
DEFINE_FWK_MODULE(IntArrayTableProducer);
DEFINE_FWK_MODULE(BoolArrayTableProducer);
